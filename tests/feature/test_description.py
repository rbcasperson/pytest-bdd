"""Test descriptions."""
from pytest_bdd import scenario


TEST_FILE_CONTENTS = """
import pytest
from pytest_bdd import given, scenario

def test_descriptions(request):
    @scenario(
        "descriptions.feature",
        "Description",
    )
    def test():
        pass

    test(request)

@given("I have a bar")
def nothing():
    pass

"""

with open("./tests/feature/description.feature") as f:
    FEATURE_FILE_CONTENTS = f.read()

EXPECTED_FEATURE_DESCRIPTION = """In order to achieve something
I want something
Because it will be cool


Some description goes here."""

EXPECTED_SCENARIO_DESCRIPTION = """Also, the scenario can have a description.

It goes here between the scenario name
and the first step."""


def test_description(request):
    """Test description for the feature."""

    @scenario("description.feature", "Description")
    def test():
        pass

    assert test.__scenario__.feature.description == EXPECTED_FEATURE_DESCRIPTION
    assert test.__scenario__.description == EXPECTED_SCENARIO_DESCRIPTION

    test(request)


def test_scenarios_are_created_when_they_have_scenario_descriptions(testdir):
    testdir.makepyfile(test_descriptions=TEST_FILE_CONTENTS)
    testdir.makefile(".feature", descriptions=FEATURE_FILE_CONTENTS)

    result = testdir.runpytest()
    result.assert_outcomes(passed=1)
