# vcf-creator-web-interface

![GitHub Pipenv locked Python version](https://img.shields.io/github/pipenv/locked/python-version/animesh-chouhan/vcf-creator-web-interface)
![license](https://img.shields.io/github/license/animesh-chouhan/vcf-creator-web-interface)

> Web interface for VCF Creator

## Links
Live Website: https://vcf-creator.herokuapp.com

Github: https://github.com/animesh-chouhan/vcf-creator-web-interface

## Setup

### Cloning the repository:

```sh
# Clone the repo
git clone https://github.com/animesh-chouhan/vcf-creator-web-interface.git
cd vcf-creator-web-interface
```

### Installing dependencies:

Using pip and requirements.txt:

```sh
pip install -r requirements.txt
```

Using Pipenv:

```sh
pipenv shell
pipenv install
```

### Running the script:

```sh
# Make view.sh executable
chmod a+x view.sh
./view.sh
```

### Docker:

```sh
docker run --rm -it  -p 8080:8080/tcp animeshsingh38/vcf-creator-web-interface
```

_For more examples and usage, please refer to the [Wiki][wiki]._

## Built With

* [vcf-creator](https://github.com/animesh-chouhan/vcf-creator) - Command-line program to generate vCard file from CSV

## Contributing

1. Fork the repo (<https://github.com/animesh-chouhan/vcf-creator-web-interface/>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

<!-- Markdown link & img dfn's -->
[license]: https://img.shields.io/github/license/animesh-chouhan/vcf-creator-web-interface
[wiki]: https://github.com/animesh-chouhan/vcf-creator-web-interface/wiki

## License
MIT License
copyright (c) 2021 [Animesh Singh Chouhan](https://github.com/animesh-chouhan). Please have a look at the [license](LICENSE) for more details.
