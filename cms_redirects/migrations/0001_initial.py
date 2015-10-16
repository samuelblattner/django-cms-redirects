# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cms.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
        ('cms', '0012_auto_20150607_2207'),
    ]

    operations = [
        migrations.CreateModel(
            name='CMSRedirect',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('old_path', models.CharField(help_text="This should be an absolute path, excluding the domain name. Example: '/events/search/'.", max_length=200, verbose_name='redirect from', db_index=True)),
                ('new_path', models.CharField(help_text="This can be either an absolute path (as above) or a full URL starting with 'http://'.", max_length=200, verbose_name='redirect to', blank=True)),
                ('response_code', models.CharField(default=b'301', help_text='This is the http response code returned if a destination is specified. If no destination is specified the response code will be 410.', max_length=3, verbose_name='response code', choices=[(b'301', b'301'), (b'302', b'302')])),
                ('page', cms.models.fields.PageField(blank=True, to='cms.Page', help_text='A link to a page has priority over a text link.', null=True, verbose_name='page')),
                ('site', models.ForeignKey(to='sites.Site')),
            ],
            options={
                'ordering': ('old_path',),
                'verbose_name': 'CMS Redirect',
                'verbose_name_plural': 'CMS Redirects',
            },
        ),
        migrations.AlterUniqueTogether(
            name='cmsredirect',
            unique_together=set([('site', 'old_path')]),
        ),
    ]
