# alkis-sampler

A command-line tool to sample and print ALKIS-style parcel templates from a GeoPackage or vector file.

## Features

- Print available columns from a GeoPackage
- Randomly sample parcel records using specific ALKIS field names
- Outputs structured templates for further use

## ⚙️ Installation

#### 1. Install `pipx` (if not already installed)

```bash
python -m pip install --user pipx
python -m pipx ensurepath
```

> Then restart your terminal.

#### 2. Install the CLI tool

From the root of this repository:

```bash
pipx install .
```

This makes the `alkis-sampler` command globally available.

## Usage

```bash
alkis-sampler <path> [<land> <field_gemarkung> <field_flur> <field_flurstueck_zaehler> <field_flurstueck_nenner> <n>]
```

### Examples

#### 1. Print available fields in the first layer:

```bash
alkis-sampler mydata.gpkg
```

#### 2. Sample 5 random ALKIS-style parcels:

```bash
alkis-sampler mydata.gpkg 12 GEMARKUNG FLUR FLST_Z FLST_N 5
```
## Development

This is a single-file CLI tool.

Project structure:
```
alkis-sampler/
├── alkis_sampler.py
└── setup.py
```

To reinstall after changes:
```bash
pipx uninstall alkis-sampler
pipx install .
```
