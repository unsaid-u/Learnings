This is a readme file of one of the pixelbin repo in fynd 
* Its has an interesting local setup process 
* generating a local SSL certificate 
* mapping localhost to that domain 
* had a sh file with all config to up the application

* For the first time i used the .npmrc file for defining a specific version of python required a sp dependency 
* for the first time used nvm, for a specific version of node 

## Hinata

Pixelbin is paid Image, Video, Text, intelligent transformation service.

Hinata - Pixelbin Frontend stack

-   React
-   Redux
-   React-router
-   Styled-Components
-   Jest

## Prerequisites

Make sure you have installed all of the following prerequisites:

-   Node.js
-   npm

## Clone the repository

To clone the repository:

1. Set up git on the machine.
   For Ubuntu:

```bash
$ sudo apt install git
```

2. Configure ssh keys with your gitlab account.

    - Log in to your gitlab account.
    - Go to edit profile and select `SSH Keys` in the sidebar.
    - Follow the links to generate and add an ssh key.

3. Clone the repo:
    - Go to the project repository on gitlab.
    - Click on `Clone` button
    - Copy the `Clone with SSH` link.
    - Open terminal.
    - Use the following command

```bash
$ git clone git@gitlab.com:fynd/regrowth/erasebg/ui/hinata.git
```

You can follow a thorough guide [here](https://docs.gitlab.com/ee/gitlab-basics/start-using-git.html#clone-a-repository)

## Setup local SSL certificate

1. First install **mkcert**. Refer this [link](https://github.com/FiloSottile/mkcert#example) to install it.
2. We will be using `mkcert` to generate locally-trusted development certificate.
   Use this command to generate SSL certificate

```bash
$ mkcert -key-file key.pem -cert-file cert.pem "*.pixelbinz0.de"
```

3. Create a folder named **ssl** at root level of repository.
4. Copy the two `.pem` files (i.e key.pem & cert.pem) generated above command to **ssl** folder

5. Next up we will bind `localhost or 127.0.0.1` to host name i.e `local.pixelbinz0.de`
6. open and edit `/etc/hosts` and insert

```bash
127.0.0.1       local.pixelbinz0.de
```

## Starting the project

To start the project locally,

1. Install the dependencies with `npm install`
2. Set the required env vars in `run.local.sh`.
3. Set permissions with

```bash
$ chmod +x ./run.local.sh
```

4. Run the script with

```bash
$ ./run.local.sh
```

Before deploying the project to upstream environments, it is advisable to test the project with docker locally.
To run project on docker locally,

1. Set the required env vars in `run.docker.sh`.
2. Set permissions with

```bash
$ chmod +x ./run.docker.sh
```

3. Run the script with

```bash
$ ./run.docker.sh
```
