# Bilibili Video Downloader

## Description

A simple well-typed bilibili video downloader.

## Environment

- Python 3.10

## Usage

### Install dependencies

```bash
pip -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Run Example

```bash
python main.py
```

## Important Detail

see `main.py`.

When create `Bilibili` instance, you can pass `cookie`.

If not `cookie` set, it can only grab videos with `480p` and `360p` resolution.

## Run Test

```bash
python -m unittest
```
