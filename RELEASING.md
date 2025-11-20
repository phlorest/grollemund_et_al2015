# Releasing

- Install in editable mode:
  ```shell
  pip install -e .[test]
  ```
- Re-create the CLDF dataset:
  ```shell
  cldfbench makecldf --glottolog-version v5.2 cldfbench_grollemund_et_al2015.py --with-zenodo --with-cldfreadme
  ```
- Make sure the CLDF is valid:
  ```shell
  pytest
  ```
- Re-create the README:
  ```shell
  cldfbench readme cldfbench_grollemund_et_al2015.py
  ```
- Run Phlorest-specific checks on the data:
  ```shell
  phlorest check --with-R cldfbench_grollemund_et_al2015.py
  ```
- Check whether new files have been generated (and add them if so):
  ```shell
  git status
  ```
- Figure out the new release tag:
  ```shell
  git tag
  ```
- Commit and push the release-ready data:
  ```shell
  git commit -a -m"release vX.Y"
  git push origin
  ```
- Create the release instruction:
  ```shell
  phlorest release cldfbench_grollemund_et_al2015.py vX.Y
  ```
- Make sure the repository is wired up with Zenodo, and if so run the `gh release` command as
  given in the output of `phlorest release`.
