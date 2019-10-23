## Updating

* Make your changes to the code/config
* If you changed the CLI tool, bump the version in `setup.py`
* Commit
* Add tag with version to the commit and push it (`git tag 1.1.9 && git push --tags`)
* In the using projects,
  * update `requirements.txt` (put the version/tag name behind the @)
  * and `.pre-commit-config.yaml` (bump `rev` to new version)
