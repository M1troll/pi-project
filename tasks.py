import inspect

# hack to support `invoke` for python 3.11
# https://github.com/pyinvoke/invoke/issues/833
if not hasattr(inspect, 'getargspec'):  # noqa
    inspect.getargspec = inspect.getfullargspec

from invoke import task


@task
def hooks(context):
    """Run git hooks."""
    context.run("pre-commit run --all-files")
