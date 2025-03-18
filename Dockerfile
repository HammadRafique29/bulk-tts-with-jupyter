FROM ghcr.io/coqui-ai/tts:latest

# Install Jupyter Notebook
RUN pip install jupyter

# Expose the Jupyter Notebook port
EXPOSE 8888

RUN apt-get update && apt-get install -y \
    wget \
    git && \
    git clone https://github.com/HammadRafique29/bulk-tts-with-jupyter.git /root/TTS/jupyter_files && \
    cp /root/TTS/jupyter_files/local_tts.ipynb /root/TTS/local_tts.ipynb

# Set the entry point to allow overriding with Jupyter Notebook
ENTRYPOINT ["jupyter", "notebook"]
CMD ["--ip=0.0.0.0", "--no-browser", "--allow-root", "--notebook-dir=/root/TTS"]
