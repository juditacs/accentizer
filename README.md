# Hunaccent

Accentize Hungarian text.

## Compiling

    g++ hunaccent.cpp -std=c++11 -O3 -Wall -pedantic -o hunaccent

## Usage

    $ echo arvizturo tukorfurogep | ./hunaccent
    árvíztűrő tükörfúrógép

If you call the binary from a different directory, you need to specify the location of the trees:

    $ echo arvizturo tukorfurogep | ./hunaccent/hunaccent hunaccent/tree/
    árvíztűrő tükörfúrógép

## Deaccentize input

    $ echo árvíztűrő tükörfúrógép | ./deaccentize.py
    arvizturo tukorfurogep


Accentizing again:

    $ echo árvíztűrő tükörfúrógép | ./deaccentize.py | ./hunaccent 
    árvíztűrő tükörfúrógép

## Note

Hunaccent is still under heavy development, meaning I might change the tree files for better ones anytime.

## Other languages

Other European languages will be added shortly.
