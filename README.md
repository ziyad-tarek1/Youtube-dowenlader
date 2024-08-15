
## Note the data will be found in /app/downloads
if you want to presist the data use VP as showen below 
docker run -p 5000:5000 -v /path/on/host/downloads:/app/downloads yt-downloader


sudo chown -R $(whoami):$(whoami) /home/ziad/Downloads
