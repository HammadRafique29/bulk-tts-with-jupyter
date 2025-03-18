@echo off
docker run -it --rm -v $(pwd):/workspace -p 8888:8888 tts_image
echo.
pause
