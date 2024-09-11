# app.py
# This is a test commit

run: |
   while read -r cmd
        do
          eval sudo $cmd
        done < <(Rscript -e 'cat(remotes::system_requirements("ubuntu", "20.04"), sep = "\n")')

def add(a, b):
    return a + b

def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0
