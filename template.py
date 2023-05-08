#!/usr/bin/env python3
import pymoddinglib as pml

def main():
    print('Running...')
    app = pml.ModdableApp('mods'), True, True)
    app.enable_all()
    app.run_mods()
    print('Done')

if __name__ == '__main__': main()
