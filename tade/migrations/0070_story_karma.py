# Generated by Django 3.1.3 on 2021-08-15 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tade", "0069_rename_context_warning_to_content_warning"),
    ]

    operations = [
        migrations.RunSQL(
            sql=[
                ("PRAGMA legacy_alter_table = TRUE;", []),
            ],
            reverse_sql=[("PRAGMA legacy_alter_table = TRUE;", [])],
        ),
        migrations.AddField(
            model_name="story",
            name="karma",
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.RunSQL(
            sql=[
                (
                    """CREATE TRIGGER tade_vote_insert AFTER INSERT ON tade_vote
                    FOR EACH ROW WHEN NEW.comment_id IS NULL
                    BEGIN
                    UPDATE tade_story
                    SET karma = (karma + 1)
                    WHERE
                        id = NEW.story_id;
                        END;""",
                    [],
                )
            ],
            reverse_sql=[("DROP TRIGGER IF EXISTS tade_vote_insert", [])],
        ),
        migrations.RunSQL(
            sql=[
                (
                    """CREATE TRIGGER tade_vote_delete AFTER DELETE ON tade_vote
                    FOR EACH ROW WHEN OLD.comment_id IS NULL
                    BEGIN
                    UPDATE tade_story
                    SET karma = (karma - 1)
                    WHERE
                        id = OLD.story_id;
                        END;""",
                    [],
                )
            ],
            reverse_sql=[("DROP TRIGGER IF EXISTS tade_vote_delete", [])],
        ),
        migrations.RunSQL(
            sql=[
                (
                    """UPDATE tade_story SET karma = (SELECT COUNT(id) FROM tade_vote AS v WHERE v.story_id = tade_story.id AND v.comment_id IS NULL);""",
                    [],
                )
            ],
            reverse_sql=[("", [])],
        ),
        migrations.AddField(
            model_name="comment",
            name="karma",
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.RunSQL(
            sql=[
                (
                    """CREATE TRIGGER tade_vote_insert_comment AFTER INSERT ON tade_vote
                    FOR EACH ROW WHEN NEW.comment_id IS NOT NULL
                    BEGIN
                    UPDATE tade_comment
                    SET karma = (karma + 1)
                    WHERE
                        id = NEW.comment_id;
                        END;""",
                    [],
                )
            ],
            reverse_sql=[("DROP TRIGGER IF EXISTS tade_vote_insert_comment", [])],
        ),
        migrations.RunSQL(
            sql=[
                (
                    """CREATE TRIGGER tade_vote_delete_comment AFTER DELETE ON tade_vote
                    FOR EACH ROW WHEN OLD.comment_id IS NOT NULL
                    BEGIN
                    UPDATE tade_comment
                    SET karma = (karma - 1)
                    WHERE
                        id = OLD.comment_id;
                        END;""",
                    [],
                )
            ],
            reverse_sql=[("DROP TRIGGER IF EXISTS tade_vote_delete_comment", [])],
        ),
        migrations.RunSQL(
            sql=[
                (
                    """UPDATE tade_comment SET karma = (SELECT COUNT(id) FROM tade_vote AS v WHERE v.story_id = tade_comment.story_id AND v.comment_id = tade_comment.id);""",
                    [],
                )
            ],
            reverse_sql=[("", [])],
        ),
        migrations.RunSQL(
            sql=[
                ("PRAGMA legacy_alter_table = TRUE;", []),
            ],
            reverse_sql=[("PRAGMA legacy_alter_table = TRUE;", [])],
        ),
    ]