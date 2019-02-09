# Copyright 2016 Evgeny Golyshev. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.db import models

from users.models import User

MENDER_ARTIFACT = 3


class TargetDevice(models.Model):
    full_name = models.CharField(max_length=80)
    short_name = models.CharField(max_length=40)


class Distro(models.Model):
    full_name = models.CharField(max_length=80)
    short_name = models.CharField(max_length=40)


class BuildType(models.Model):
    full_name = models.CharField(max_length=80)


class UnknownBuildTypeId(Exception):
    """Exception raised when attempting to get an unknow build type. """


class Firmware(models.Model):
    DONE = 'done'
    FAILED = 'failed'
    BUILDING = 'building'
    INITIALIZED = 'initialized'
    TAR_GZ = 'tar.gz'
    IMG_GZ = 'img.gz'
    ART_MENDER = 'mender'
    STATUS_CHOICES = (
        (DONE, 'Done'),
        (FAILED, 'Failed'),
        (BUILDING, 'Building'),
        (INITIALIZED, 'Initialized')
    )
    FORMAT_CHOISES = (
        (TAR_GZ, 'Old tar.gz'),
        (IMG_GZ, 'New img.gz'),
        (ART_MENDER, 'Mender artifact')
    )
    name = models.CharField(max_length=36)
    user = models.ForeignKey(User)
    status = models.CharField(
        max_length=11,
        choices=STATUS_CHOICES,
        default=DONE,
    )
    started_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        blank=True,
        null=True,
    )
    finished_at = models.DateTimeField(
        blank=True,
        null=True,
    )
    log = models.TextField(blank=True)
    pro_only = models.BooleanField(
        default=False
    )
    format = models.CharField(
        max_length=6,
        choices=FORMAT_CHOISES,
        default=TAR_GZ,
    )
    targetdevice = models.ForeignKey(
        TargetDevice,
        blank=True,
        null=True,
    )
    distro = models.ForeignKey(
        Distro,
        blank=True,
        null=True,
    )
    build_type = models.ForeignKey(
        BuildType,
        blank=True,
        null=True,
    )
    notes = models.TextField(
        default='',
    )

    def set_build_type(self, build_type_id):
        self.build_type = BuildType.objects.get(pk=build_type_id)
        if self.build_type is None:
            raise UnknownBuildTypeId('Unknow build_type_id {}'.format(build_type_id))
        if self.build_type.id == MENDER_ARTIFACT:
            self.format = Firmware.ART_MENDER
        else:
            self.format = Firmware.IMG_GZ
