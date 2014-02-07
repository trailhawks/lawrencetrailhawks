# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Race.latitude'
        db.add_column(u'races_race', 'latitude',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=6, blank=True),
                      keep_default=False)

        # Adding field 'Race.longitude'
        db.add_column(u'races_race', 'longitude',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=6, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Race.latitude'
        db.delete_column(u'races_race', 'latitude')

        # Deleting field 'Race.longitude'
        db.delete_column(u'races_race', 'longitude')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'members.member': {
            'Meta': {'ordering': "['last_name']", 'object_name': 'Member'},
            'address': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'address2': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'avatar': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'date_paid': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'gender': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'hawk_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'member_since': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'receive_comment_emails': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'username': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'})
        },
        u'races.emergencycontact': {
            'Meta': {'object_name': 'EmergencyContact'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '13'}),
            'relationship': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        u'races.race': {
            'Meta': {'ordering': "['-start_datetime']", 'object_name': 'Race'},
            'annual': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'awards': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'course_map': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'cut_off': ('django.db.models.fields.CharField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'discounts': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'distance': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'entry_form': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '6', 'blank': 'True'}),
            'location': ('django.db.models.fields.TextField', [], {}),
            'location_iframe': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'lodging': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '6', 'blank': 'True'}),
            'map_link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'packet_pickup': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'race_directors': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['members.Member']", 'symmetrical': 'False'}),
            'race_type': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'reg_description': ('django.db.models.fields.TextField', [], {}),
            'reg_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'slogan': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'sponsors': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'sponsors'", 'symmetrical': 'False', 'to': u"orm['sponsors.Sponsor']"}),
            'start_datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'unit': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        },
        u'races.racer': {
            'Meta': {'ordering': "['last_name', 'first_name']", 'object_name': 'Racer'},
            'birth_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['races.EmergencyContact']", 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'gender': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '13', 'null': 'True', 'blank': 'True'}),
            'shirt_size': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'trailhawk': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['members.Member']", 'unique': 'True', 'null': 'True', 'blank': 'True'})
        },
        u'races.racetype': {
            'Meta': {'object_name': 'RaceType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'blank': 'True'})
        },
        u'races.registration': {
            'Meta': {'object_name': 'Registration'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'race': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['races.Race']"}),
            'reg_cost': ('django.db.models.fields.IntegerField', [], {}),
            'reg_date': ('django.db.models.fields.DateField', [], {})
        },
        u'races.report': {
            'Meta': {'object_name': 'Report'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'race': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['races.Race']"}),
            'racer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['races.Racer']"}),
            'report': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'races.result': {
            'Meta': {'ordering': "('time',)", 'object_name': 'Result'},
            'bib_number': ('django.db.models.fields.IntegerField', [], {}),
            'course_record': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'dnf': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'dns': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'dq': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'place': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'race': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['races.Race']"}),
            'race_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['races.RaceType']", 'null': 'True', 'blank': 'True'}),
            'racer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['races.Racer']"}),
            'time': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        },
        u'sponsors.sponsor': {
            'Meta': {'object_name': 'Sponsor'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'address': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']", 'null': 'True', 'blank': 'True'}),
            'discount_detail': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['races']