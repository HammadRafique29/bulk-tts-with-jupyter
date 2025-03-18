@echo off
docker run -it --rm --gpus all -v $(pwd):/workspace -p 8888:8888 magtronix_tts_image
echo.
pause
