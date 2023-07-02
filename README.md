# Flask Advanced Template

## Introduction

This is an advanced Flask web application template.

## Setting up

On Ubuntu operating system, you can simply run `setup.sh` to install everything needed to run the web application:

```bash
./setup.sh
```

Then, you can run the web application by running `run.sh`:

```bash
./run.sh
```

**Note**: In order to modify the config of the web application, you can create a `.env` file in the root directory as explained [here](https://www.npmjs.com/package/dotenv).

**Note**: You can modify admin properties by editing the second line of `run.sh` before running:

```bash
flask users create-admin USERNAME EMAIL PASSWORD
```

## Requirements

### Overall Packages

| Package | Version | Description |
| --- | --- | --- |
| python3 | 3.11.2 | A programming language that lets you work quickly and integrate systems more effectively |
| python3-pip | 23.0.1 | The PyPA recommended tool for installing Python packages |
| python3-venv | 3.11.2-1 | Supports creating lightweight virtual environments |
| mongod | 6.0.7 | A source-available cross-platform document-oriented database program

### Python Packages

| Package | Version | Description |
| --- | --- | --- |
| Flask | 2.3.2 | A simple framework for building complex web applications |
| Flask-Assets | 2.0 | Asset management for Flask, to compress and merge CSS and Javascript files |
| Flask-WTF | 1.1.1 | Form rendering, validation, and CSRF protection for Flask with WTForms |
| Flask-Login | 0.6.2 | User authentication and session management for Flask |
| MongoEngine | 0.27.0 | A Python Object-Document Mapper for working with MongoDB |
| jsmin | 3.0.1 | JavaScript minifier |
| rcssmin | 1.1.1 | CSS Minifier |
| python-dotenv | 1.0.0 | Read key-value pairs from a `.env` file and set them as environment variables |
| email-validator | 2.0.0.post2 | A robust email address syntax and deliverability validation library |

## Contributing

I welcome contributions! Please refer to [CONTRIBUTING.md](/CONTRIBUTING.md) for details on the code of conduct, and the process for submitting pull requests.

## Founder

This repository was founded by [*Kazem Forghani*](https://github.com/k-forghani), a student of Computer Science Department of Iran University of Science and Technology.

You can contact via k_forghani@mathdep.iust.ac.ir.

## License

This repository has been released under *MIT License*.