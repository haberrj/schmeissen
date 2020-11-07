[Table of Contents](../README.md)

## Contributing

For now, we'll use the ```python``` virtual environment. Just until we figure 
out the Docker settings and configurations.

### First time setup

This is mainly for James.

1.  Fork the repository from [here](https://github.com/haberrj/schmeissen).
2.  Clone your forked repository.

    ```
    $ git clone https://github.com/{username}/schmeissen.git
    $ cd schmeissen
    ```

3.  Add the original repository as a remote repository called ```upstream```.

    ```
    $ git remote add upstream https://github.com/haberrj/schmeissen.git
    ```

4.  Make sure you have python3 and pip installed.

    Linux/Mac/Windows
    ```
    $ python3 --version
    $ pip3 --version
    ```

5.  Create your virtual environment and activate it.

    Linux/Mac
    ```
    $ python3 -m venv venv
    $ source venv/bin/activate
    ```

    Windows
    ```
    $ py -3 -m venv venv
    $ venv/Scripts/activate
    ```

6.  Install the dependencies.

    Linux/Mac/Windows
    ```
    $ pip install -r requirements.txt
    ```

### Before working on your contributions

1.  Pull any changes made to the original repository and merge them to your 
    master branch.

    ```
    $ git fetch upstream

    $ git checkout master

    $ git merge upstream/master
    ```

### Running the local environment

I'll write a bash script to automate this process somewhere down the line.

For every sub-stack, make sure you're in the top-level directory, you've 
activated the virtual environment, and all of your local dependencies are 
up-to-date with the master repo before running any of the below commands.

#### Main Server

1.  Run the ```Flask``` development server (normally we use ```$ flask run```, 
    but we have to run via the SocketIO library for WebSocket support).

    ```
    $ python schmeissen.py
    ```

#### Email Server

1.  Run the built-in ```Python``` SMTP server.

    ```
    $ python -m smtpd -n -c DebuggingServer localhost:8025
    ```

### Making changes

```TODO```