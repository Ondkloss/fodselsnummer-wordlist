# Usage

To create a `txt` file containing all fødselsnummer simply run:

    python fodselsnummer.py

You can limit the input range for `days`, `months` and `years` if some of these values are more fixed.

## Fair warning

This is not a very fast program.

## John the Ripper

This can be used to, for example, recover PDFs that have a "open password" which you know to be a fødselsnummer.

Example sequence of events:

    python fodselsnummer.py
    perl pdf2john.pl mypdf.pdf > mypdf.hash
    john --wordlist=fodselsnummer.txt mypdf.hash
