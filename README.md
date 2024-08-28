# YouTube Downloader with Flask & Docker

This project is a simple YouTube downloader built with Flask and `yt-dlp`, designed to allow users to download single videos or entire playlists from YouTube. The application is containerized with Docker for easy deployment and scaling.

## Features

- **Download YouTube Videos:** Easily download individual videos from YouTube by providing the video URL.
- **Download Playlists:** Download entire playlists with a single click.
- **User-Friendly Interface:** Simple and intuitive web interface built with HTML, CSS, and Flask.
- **Containerized with Docker:** Easily deploy the application using Docker, ensuring consistent performance across different environments.

## Getting Started

### Prerequisites

- Docker installed on your machine
- Basic understanding of Flask and Docker

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/ziyadtarek99/Youtube-dowenlader.git
   cd Docker
2. **Build the Docker image:**
   ```bash
   docker build -t youtube-downloader .

3. **Run the Docker container:**

    ```bash
   docker run -d -p 5000:5000 youtube-downloader


## Note the data will be found in /app/downloads
if you want to presist the data use VP as showen below 
docker run -p 5000:5000 -v /path/on/host/downloads:/app/downloads yt-downloader
sudo chown -R $(whoami):$(whoami) /home/ziad/Downloads

4. **Access the application:**

Open your web browser and navigate to http://localhost:5000.

**Usage**
  1- Enter the URL of the YouTube video or playlist you want to download.
  2- Select whether you want to download a single video or an entire playlist.
  3-Click the "Download" button.
  4-The application will display a success or error message based on the download outcome.
**Project Structure**
  app.py: Main Flask application file.
  templates/index.html: HTML template for the web interface.
  static/styles.css: CSS file for styling the web interface.
  Dockerfile: Docker configuration file for building the container.
  requirements.txt: Python dependencies for the project.
  Technologies Used
  Flask: Python web framework.
  yt-dlp: Command-line program to download videos from YouTube.
  Docker: Containerization platform for consistent deployment.

Contact
For any inquiries or issues, please feel free to contact me via Gmail (ziyadtarek180@gmail.com) Linkedin(https://www.linkedin.com/in/ziyad-tarek-61a38818b/)
