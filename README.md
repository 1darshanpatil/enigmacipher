![enigma-cipher](https://github-production-user-asset-6210df.s3.amazonaws.com/72539638/288369435-7ed29d47-177b-4c86-bc12-c3517dd9a67c.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIWNJYAX4CSVEH53A%2F20231206%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231206T103912Z&X-Amz-Expires=300&X-Amz-Signature=77ae7d2fdcf704315037b56e8a3566f80aa39c4932077f6b667fc650444f8847&X-Amz-SignedHeaders=host&actor_id=72539638&key_id=0&repo_id=728136182)


# EnigmaCipher

A Python package that simulates the encryption and decryption mechanisms of an Enigma machine with PIN protection.

## Capabilities
 * Utilize the shuffle command to introduce new rotors
 * Securely encrypt and decrypt messages with a PIN-based system

## Installation

To install EnigmaCipher, simply run:

```bash
pip install enigmacifra
```

Verify the installation by checking the version: 

```bash
$ enigma --version
```

## Usage

The EnigmaCipher package can be used via the command line.

### Command Line

To shuffle rotors:

```bash
$ enigma shuffle
```

To encrypt a message:

```bash
$ enigma encrypt
```

To decrypt a message:
 
```bash
$ enigma decrypt
```



## Development

To contribute to EnigmaCipher, clone the repository and make sure to install the development dependencies.

```bash
git clone https://github.com/1darshanpatil/enigmacipher
cd enigmacipher
pip install -e .
```

## Support

If you encounter any problems or have suggestions, please file an issue on the [GitHub issue tracker](https://github.com/1darshanpatil/enigmacipher/issues).

## License

The project is licensed under the MIT license.
