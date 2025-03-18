# 🚀 Bulk TTS with Jupyter
### Bulk TTS-xtts_v2 - Audio Generation with Docker & Jupyter

Bulk TTS with Jupyter enables users to generate high-quality text-to-speech (TTS) audio files using the xtts_v2 model. This project leverages Docker for easy setup and Jupyter Notebooks for batch processing, making it ideal for large-scale audio generation tasks.
With support for **multi-language** synthesis and **custom voices**, this tool is well-suited for voiceovers, accessibility solutions, and AI-driven audio applications.


<br>

# 📌 Installation


### 1️⃣ Install Required Dependencies
- Download & Install **Docker**
- Download the **Xtts_v2 model** from [HammadRafique02 Drive](https://drive.google.com/file/d/1e3aPJHaZRi3CvdEim7eRQPO_AODHkzDF/view?usp=sharing) and extract it in your `Documents` folder.
  - Example path: `C:\Users\username\Documents\tts_models\tts_models--multilingual--multi-dataset--xtts_v2`

### 2️⃣ Build the Docker Image

  - #### 🖥️ Windows
    ```sh
    docker build -t magtronix_tts_image .
    ```

  - #### 🐧 Linux
    ```sh
      sudo docker build -t magtronix_tts_image .
    ```


### 3️⃣ Run the Docker Container
- Start the container (with or without GPU support, see below)
- Wait for Docker logs to initialize
- Open the provided URL in your browser:
  ```
  http://127.0.0.1:8888/tree?token=YOUR_UNIQUE_TOKEN
  ```


### 4️⃣ Configure the Jupyter Notebook
- Open `local_tts.ipynb`
- Modify the following parameters:
  - **Excel Sheet ID:** [Sample Sheet](https://docs.google.com/spreadsheets/d/1BGuyZ-mkJ0L2O_nztQko8OrYjs0MJBu98t2-57HdKjc/edit?gid=0#gid=0)
  - **Enter** `VOICE_TYPE` & `Language`
- **Restart & Run All Cells**


### 5️⃣ Final Step
- Wait for TTS processing to complete
- A **download link** will appear in the output of the last cell
- Output includes:
  - 🎵 **Generated audio files**
  - 🎙️ **Speaker details**
  - 📊 `data.xlsx` containing metadata

<br>

## ⚡ Running with GPU

Using a GPU significantly improves TTS processing speed. Below are the commands for different platforms:

- ### 🖥️ Windows (Command Prompt)
  ```sh
    docker run -it --rm --gpus all ^
      -v "C:\Users\Magician\Documents\tts_models:/root/.local/share/tts" ^
      -p 8888:8888 magtronix_tts_image
  ```

- ### 🖥️ Windows (PowerShell)
  ```sh
    docker run -it --rm --gpus all `
      -v "C:\Users\Magician\Documents\tts_models:/root/.local/share/tts" `
      -p 8888:8888 magtronix_tts_image
  ```

- ### 🐧 Linux (Bash)
  ```sh
    docker run -it --rm --gpus all \
      -v "/home/your_username/Documents/tts_models:/root/.local/share/tts" \
      -p 8888:8888 magtronix_tts_image
  ```

<br>

## 💻 Running with CPU

If your system lacks GPU support, you can still run the TTS model using CPU-only mode.

- ### 🖥️ Windows (Command Prompt)
  ```sh
    docker run -it --rm  ^
      -v "C:\Users\Magician\Documents\tts_models:/root/.local/share/tts" ^
      -p 8888:8888 magtronix_tts_image
  ```

- ### 🖥️ Windows (PowerShell)
  ```sh
    docker run -it --rm `
      -v "C:\Users\Magician\Documents\tts_models:/root/.local/share/tts" `
      -p 8888:8888 magtronix_tts_image
  ```

- ### 🐧 Linux (Bash)
  ```sh
    docker run -it --rm \
      -v "/home/your_username/Documents/tts_models:/root/.local/share/tts" \
      -p 8888:8888 magtronix_tts_image
  ```

<br>

## 🔧 Default Running Command
  - ```sh
    docker run -it --rm --gpus all -v $(pwd):/workspace -p 8888:8888 magtronix_tts_image
    ```

<br>


## 🛠️ Facing GPU Issues?
If you're experiencing GPU-related issues, try running the following command to check if your GPU is detected correctly:
```sh
docker run --rm --gpus all nvidia/cuda:12.0-base nvidia-smi
```
Then, restart the Docker container and retry running the Jupyter Notebook.

<br>

## 🎯 Suggested Enhancements
- **Integrate API Support**: Adding a REST API for batch processing could allow external applications to interact with the TTS engine.
- **Pre-built Docker Image**: Hosting a pre-built Docker image on Docker Hub would simplify setup for users.

<br>

## 🎯 Final Step
- Wait for logs and open the Jupyter Notebook URL:
  ```
  http://127.0.0.1:8888/tree?token=YOUR_UNIQUE_TOKEN
  ```

<br>

## 💖 Support the Project

I open-source almost everything I can and try my best to help others who use these projects. This takes time and effort, and I offer it for free.

If you find this project useful and want to support its development, here are a few ways you can help:

✅ **Give Proper Credit**: If you use this project, linking back to it would be appreciated.  
⭐ **Star & Share**: Starring and sharing the repository helps spread the word! 🚀  
💰 **Donate BTC**: If you'd like to support my work, you can send Bitcoin donations to the following address:  


Every bit of support helps and motivates me to continue improving and creating open-source projects.  

Thank you! ❤️  

<br>

## 📫 Contact Me

Feel free to reach out or follow my work:

- **GitHub**: [HammadRafique029](https://github.com/HammadRafique029)  
- **LinkedIn**: [Hammad Rafique](https://www.linkedin.com/in/hammad-rafique-hr029/)  



