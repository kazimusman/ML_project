## ML_project
This is my first ML project

### Software and acount requirement: 
1. [Github Account](https://github.com/)
2. [Heroku Account](https://id.heroku.com/login)
3. [VS Code IDE](https://code.visualstudio.com/download)
4. [Git cli](https://git-scm.com/downloads)
5. [Git Documentation](https://git-scm.com/docs/gittutorial)


Creating conda environment(virtual environment venv)

```
conda create -p venv python==3.7 -y 
```

To activate conda
```
conda activate /Users/kazimusman/projects/ML_project/venv
```


Command to install flask
```
pip install -r requirements.txt
```


To add files to git
```
git add .
OR 
git add <filename>
```

Note: To ignore file or folder from git we can write name of file/folder in gitignore file

To check the git status
```
git status
```
To check all version maintained by git
```
git log
```
To create version/commit all changes by git
```
git commit -m "message"
```
To send version/changes to github
```
git push origin main
```

To check remote URL
```
git remote -v
```
To setup CI/CD pipeline in heroku we need 3 information

1. HEROKU_EMAIL = kazimusman@yahoo.com
2. HEROKU_API_KEY = <>
3. HEROKU_APP_NAME = ml-regression11-app


BUILD DOCKER IMAGE
```
docker build -t <image_name>:<tagname> .
```

Note: image name for docker must be lowercase

To list docker image
```
docker images
```
Run docker image 
```
docker run -p 5000:5000 -e PORT=5000 <image id>
```
To check running container in docker
```
docker ps
```
to stop docker container
```
docker stop <container_id>
```

```
python setup.py install
```

install ipykernel . To run jupyter notebook inside vs code 
```
pip install ipykernel
```

DATA DRIFT:
When your dataset stats gets changes we call it as data drift.
We try to check statistics of one dataset with other dataset and if the statistics of both dataset are same then
we say it zero percent data drift. If both datasets have huge amount of statistical difference then we call it as 
data drift.  

## Write a function to get training file path from artifact dir