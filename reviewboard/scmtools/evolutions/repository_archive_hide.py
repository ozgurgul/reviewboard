"""Hide repositories that were archived before archiving hid them.

Version Added:
    10.0
"""

from __future__ import annotations

from django_evolution.mutations import SQLMutation


MUTATIONS = [
    SQLMutation('hide_archived_repositories', ["""
        UPDATE scmtools_repository
           SET visible = FALSE
         WHERE archived
"""]),
]
