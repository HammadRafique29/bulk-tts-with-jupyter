FROM ghcr.io/coqui-ai/tts:latest

# Install Jupyter Notebook
RUN pip install jupyter

# Set the working directory
WORKDIR /workspace

# Expose the Jupyter Notebook port
EXPOSE 8888

# Set the entry point to allow overriding with Jupyter Notebook
ENTRYPOINT ["jupyter", "notebook"]
CMD ["--ip=0.0.0.0", "--no-browser", "--allow-root", "--notebook-dir=/root/TTS"]