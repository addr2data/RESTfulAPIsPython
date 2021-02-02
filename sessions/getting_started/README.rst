Getting Started
===============

Prereqs
-------
- Make sure you have Python (3.8.1 or later), Pip (latest) and Git installed.
- If you don’t have a GitHub account, please create one.
- Send me your GitHub username.
- Add your public SSH key to your GitHub account (generate new keys if necessary).
- Create a new repo for this training.
- Do a little research and decide where you want to write Python. I use Sublime Text (Python aware text editor). You could also use an IDE (PyCharm is very common).
- **Verify your access to the 'Working with RESTful APIs in Python' channel under the 'API Users' team**
- **Simulators are under files**
- **Links and recording are under Useful Stuff**


Sync with your repo via ssh
---------------------------
- mdkir <your-repo-name>
- cd <your-repo-name>
- git init
- git remote add origin <path-to-repo>
- git status
- git add *
- git status
- git commit -m "initial commit"
- git push origin master


Sync with this repo via ssh (or https)
--------------------------------------
- git clone git@github.com:addr2data/RESTfulAPIsPython.git
- **or if ssh fails**
- git clone https://github.com/addr2data/RESTfulAPIsPython.git
- git pull origin master (to get updates)

Execute script **sample.py**
----------------------------
- cd session/getting_started
- python sample.py


Execute script **ex_01.py**
----------------------------
- cd session/getting_started
- python ex_01.py


Review example from Ken
-----------------------
- cd session/getting_started
- From shell: sed -e 's/launchpad/10.5.2.1/g' file-from-ken.json > new-file.json
- delete new-file.json
- Modify ex_02.py
- python ex_02.py
