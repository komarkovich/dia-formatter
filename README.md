# Dia-formatter - LocalStack diagnosis log formatter
Format LocalStack diagnostics files in to human readable form. 

Users of [LocalStack](https://github.com/localstack/localstack) can create diagnostics reports via the diagnostics endpoint:

```shell
curl -s localhost:4566/_localstack/diagnose | gzip -cf > diagnose.json.gz
```

Raw report is not in human readable form and needs to be further formated.  

`dia-formatter` helps with that, by formatting it into a human readable form. 

# Installation

Just clone the repository to your local machine with `git clone https://github.com/komarkovich/dia-formatter/` 

# Usage

## Format diagnostics report

After cloaning the repository, you can use dia-formatter like this:
```shell
python dia-formatter.py /path/to/diagnose.json.gz
```

## Formatted file 

By default the output file is stored in the same directory with a name `formatted.json`
You can change the name and folder by adding a second parameter 
```shell
python dia-formatter.py /path/to/diagnose.json.gz /path/to/formatted-file.json
```

## Input file 

dia-formatter takes as input raw `.json` files or archived `.gz` or `.zip` files. 
