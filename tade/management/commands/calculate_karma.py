from django.core.management.base import BaseCommand
from django.db import connection


class Command(BaseCommand):
    help = "Recalculate user and story karma from Vote objects"

    def handle(self, *args, **kwargs):
        with connection.cursor() as cursor:
            cursor.execute(
                "UPDATE tade_story SET karma = (SELECT COUNT(id) FROM tade_vote AS v WHERE v.story_id = tade_story.id AND v.comment_id IS NULL);",
                [],
            )
            cursor.execute(
                "UPDATE tade_comment SET karma = (SELECT COUNT(id) FROM tade_vote AS v WHERE v.story_id = tade_comment.story_id AND v.comment_id = tade_comment.id);",
                [],
            )
