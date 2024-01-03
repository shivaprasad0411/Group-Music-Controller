# Group-Music-Controller

This repository contains the code for developing a application for group music sessions where users can join a room and listen to the music in a group and can also change the song if a particular amount of users agree.

## Setup Instructions

### Install Required Python Modules

```bash
pip install -r requirements.txt
```
### Start Web Server

To start the web server you need to run the following sequence of commands.

- In the Group-Music-Controller directory run the following command.
```bash
python3 manage.py runserver
```

### [Install Node.js](https://nodejs.org/en/)

### Install Node Modules

First cd into the ```frontend``` folder.
```bash
cd frontend
```
Next install all dependicies.
```bash
npm i
```

### Compile the Front-End

Run the production compile script
```bash
npm run build
```
or for development:
```bash
npm run dev
```