## Run an AWS Lambda with Python

1. Create a lamda for Python 2.7 handler.

2. Write the `lambda_handler` in a python script (has to be called `lambda_function.py` unless configured otherwise).

3. Create a zip file for uploading:

Install pytz package

```bash
pip install pytz -t .
```

This will create `pytz` and `pytz-2016.3.dist-info` directories.

Next zip the lib directories and the `lambda_function.py` file into a file called `lambda_function.zip`

```bash
zip lambda_function -r *
```

Then upload the zip file.

4. Test and save

This example is made for event objects created by the standard API Gateway integration. For testing use
```json
{
  "params" : {
      "querystring" : {
          "fruit" : "\u308A\u3093\u3054"
      }
   }
}
```

### Resources

- http://docs.aws.amazon.com/lambda/latest/dg/lambda-python-how-to-create-deployment-package.html


