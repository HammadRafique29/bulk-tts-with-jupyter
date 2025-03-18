from platformdirs import user_documents_dir
from threading import Thread
from queue import Queue
import docker, re, time, os

get_tts_model_dir = lambda: os.path.join(str(user_documents_dir()), "tts_models")


def stop_jupyter_Container():
    client = docker.from_env()
    try:
        container = client.containers.get("magtronix_tts_container")
        container.remove(force=True)
        print("Container stopped and removed successfully.")
    except docker.errors.NotFound:
        print("Container not found. It may not be running.")
    except Exception as e:
        print(f"Error stopping container: {e}")


def run_tts_jupyter(gpu=False):

    client = docker.from_env()
    container = None
    jupyter_notebook_url = None
    temp_queue = Queue()

    try:
        container_kwargs = {
            "image": "magtronix_tts_image",
            "detach": True,
            "auto_remove": True,
            "tty": True,
            "stdin_open": True,
            "ports": {8888: 8888},
            "volumes": {get_tts_model_dir(): {"bind": "/root/.local/share/tts", "mode": "rw"}},
            "name": "magtronix_tts_container"
        }
        if gpu:
            container_kwargs["runtime"] = "nvidia"

        def run_tts_docker():

            container = None

            try:
                container = client.containers.run(**container_kwargs)
                print(f"Container started with ID: {container.id}")

                time.sleep(5)

                jupyter_notebook_url = None
                log_buffer = ""
                
                for log in container.logs(stream=True):
                    log_chunk = log.decode("utf-8")
                    log_buffer += log_chunk

                    if "\n" in log_buffer:

                        lines = log_buffer.split("\n")
                        for line in lines[:-1]:

                            # Try matching the Jupyter Notebook URL directly
                            url_match = re.search(r"(http://127\.0\.0\.1:\d+/\?token=\S+)", line)
                            if url_match:
                                jupyter_notebook_url = url_match.group(1)
                                break

                            # Alternatively match a URL with the tree endpoint
                            if "http://127.0.0.1:8888/tree?" in line:
                                jupyter_notebook_url = line
                                break
                        
                        log_buffer = lines[-1]
                        
                        if jupyter_notebook_url: break

                if jupyter_notebook_url: temp_queue.put((True, jupyter_notebook_url.split(" ")[-1])) 
                else:  raise Exception(f"TTS - Jupyter URL not found {jupyter_notebook_url}")
            
                
            except Exception as e:
                if container:
                    try: container.stop()
                    except Exception as er: pass
                temp_queue.put((False, str(e)))

        t1 = Thread(target=run_tts_docker, daemon=True)
        t1.start()
        t1.join()

        results = temp_queue.get()
        if results[0]: return {"rtn": "response/str", "value": results[1].replace("\r", "")}
        else: raise Exception(results[1])

    except Exception as e: 
        if "nvidia-container-cli: initialization error: WSL environment" in str(e):
            raise Exception(f"Starting TTS - Jupyter Failed: Graphic Card Not Supported")
        else: raise Exception(f"Starting TTS - Jupyter Failed:", e)



print(run_tts_jupyter(gpu=False))

# time.sleep(10)

# stop_jupyter_Container()