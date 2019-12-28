# lambda_twbot

Based on
- [twbot](https://github.com/gkzz/twbot)

## TL;DR

```
$ git clone 
$ aws configure
$ sudo npm install -g serverless
$ serverless create \
> --template aws-python3 \
> --name src \
> --path src
$ sudo npm install --save serverless-python-requirements
$ sudo npm install --save serverless-dotenv-plugin
$ sudo npm install --save serverless-offline
$ cat config/.env.tmpl > config/.env
$ serverless deploy
```

```
 tree -L 2
.
└── src                   
    ├── 37                 
    ├── config             
    ├── handler.py        
    ├── node_modules
    ├── package.json
    ├── package-lock.json
    ├── __pycache__
    ├── requirements.txt   
    ├── serverless.yml     
    └── serverless.yml.org

5 directories, 6 files
```