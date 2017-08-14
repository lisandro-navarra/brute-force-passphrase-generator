# brute-force-passphrase-generator

A brute force approach to generating passphrases using Python

# The problem:
        A customer has encrypted some data to secure it during transport.  Unfortunately when they attempted to decrypt the data, their passphrase did not work.  They've asked us for help in recovering their data.  Based on what we know about the encryption technology used, we're going to use a brute-force approach to try to break the passphrase.  We already have tools to run a given passphrase against this sort of encrypted data, so what we need is a list of the passphrases to try against the data.

        The passphrase that the customer *thought* they used to encrypt the data is:

                fl38Cd%mr.ypJ

# What is needed:
        A way to generate all of the possible passphrases that they might have accidentally used instead of the above passphrase.
