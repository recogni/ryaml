# ryaml

A `yaml.Loader` implementation that supports including external yaml files

## What

This library extends the `pyyaml` `Loader` to allow `!include` directives in the yaml grammar.  This serves as a drop-in replacement for the default `Loader` implemented in the `pyyaml` project.

## Install

```
git clone https://github.com/recogni/yaml
cd yaml
python setup.py install
```

## Usage

See `example/example.py`.
