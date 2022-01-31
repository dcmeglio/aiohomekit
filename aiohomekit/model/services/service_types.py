#
# Copyright 2019 aiohomekit team
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
#


class ServicesTypes:
    """
    All known service types.

    There is no centralised repository for all of these.

    * Some have by reverse engineered by open source projects like HAP-NodeJS
    * Some are "self documenting" (the name appears in the API endpoints)
    * Some are documented in open source
    """

    ACCESSORY_INFORMATION = "0000003E-0000-1000-8000-0026BB765291"
    ACCESSORY_METRICS = "00000270-0000-1000-8000-0026BB765291"
    ACCESSORY_RUNTIME_INFORMATION = "00000239-0000-1000-8000-0026BB765291"
    ACCESS_CODE = "00000260-0000-1000-8000-0026BB765291"
    ACCESS_CONTROL = "000000DA-0000-1000-8000-0026BB765291"
    AIR_PURIFIER = "000000BB-0000-1000-8000-0026BB765291"
    AIR_QUALITY_SENSOR = "0000008D-0000-1000-8000-0026BB765291"
    ASSET_UPDATE = "00000267-0000-1000-8000-0026BB765291"
    ASSISTANT = "0000026A-0000-1000-8000-0026BB765291"
    AUDIO_STREAM_MANAGEMENT = "00000127-0000-1000-8000-0026BB765291"
    BATTERY_SERVICE = "00000096-0000-1000-8000-0026BB765291"
    BRIDGE_CONFIGURATION = "000000A1-0000-1000-8000-0026BB765291"
    BRIDGING_STATE = "00000062-0000-1000-8000-0026BB765291"
    CAMERA_CONTROL = "00000111-0000-1000-8000-0026BB765291"
    CAMERA_OPERATING_MODE = "0000021A-0000-1000-8000-0026BB765291"
    CAMERA_RECORDING_MANAGEMENT = "00000204-0000-1000-8000-0026BB765291"
    CAMERA_RTP_STREAM_MANAGEMENT = "00000110-0000-1000-8000-0026BB765291"
    CARBON_DIOXIDE_SENSOR = "00000097-0000-1000-8000-0026BB765291"
    CARBON_MONOXIDE_SENSOR = "0000007F-0000-1000-8000-0026BB765291"
    CLOUD_RELAY = "0000005A-0000-1000-8000-0026BB765291"
    CONTACT_SENSOR = "00000080-0000-1000-8000-0026BB765291"
    DATA_STREAM_TRANSPORT_MANAGEMENT = "00000129-0000-1000-8000-0026BB765291"
    DIAGNOSTICS = "00000237-0000-1000-8000-0026BB765291"
    DOOR = "00000081-0000-1000-8000-0026BB765291"
    DOORBELL = "00000121-0000-1000-8000-0026BB765291"
    FAN = "00000040-0000-1000-8000-0026BB765291"
    FAN_V2 = "000000B7-0000-1000-8000-0026BB765291"
    FAUCET = "000000D7-0000-1000-8000-0026BB765291"
    FILTER_MAINTENANCE = "000000BA-0000-1000-8000-0026BB765291"
    GARAGE_DOOR_OPENER = "00000041-0000-1000-8000-0026BB765291"
    HEATER_COOLER = "000000BC-0000-1000-8000-0026BB765291"
    HUMIDIFIER_DEHUMIDIFIER = "000000BD-0000-1000-8000-0026BB765291"
    HUMIDITY_SENSOR = "00000082-0000-1000-8000-0026BB765291"
    INPUT_SOURCE = "000000D9-0000-1000-8000-0026BB765291"
    IRRIGATION_SYSTEM = "000000CF-0000-1000-8000-0026BB765291"
    LEAK_SENSOR = "00000083-0000-1000-8000-0026BB765291"
    LIGHTBULB = "00000043-0000-1000-8000-0026BB765291"
    LIGHT_SENSOR = "00000084-0000-1000-8000-0026BB765291"
    LOCK_MANAGEMENT = "00000044-0000-1000-8000-0026BB765291"
    LOCK_MECHANISM = "00000045-0000-1000-8000-0026BB765291"
    MICROPHONE = "00000112-0000-1000-8000-0026BB765291"
    MOTION_SENSOR = "00000085-0000-1000-8000-0026BB765291"
    NFCACCESS = "00000266-0000-1000-8000-0026BB765291"
    OCCUPANCY_SENSOR = "00000086-0000-1000-8000-0026BB765291"
    OUTLET = "00000047-0000-1000-8000-0026BB765291"
    PAIRING = "00000055-0000-1000-8000-0026BB765291"
    POWER_MANAGEMENT = "00000221-0000-1000-8000-0026BB765291"
    PROTOCOL_INFORMATION = "000000A2-0000-1000-8000-0026BB765291"
    SECURITY_SYSTEM = "0000007E-0000-1000-8000-0026BB765291"
    SERVICE_LABEL = "000000CC-0000-1000-8000-0026BB765291"
    SIRI = "00000133-0000-1000-8000-0026BB765291"
    SIRI_ENDPOINT = "00000253-0000-1000-8000-0026BB765291"
    SLAT = "000000B9-0000-1000-8000-0026BB765291"
    SMART_SPEAKER = "00000228-0000-1000-8000-0026BB765291"
    SMOKE_SENSOR = "00000087-0000-1000-8000-0026BB765291"
    SPEAKER = "00000113-0000-1000-8000-0026BB765291"
    STATEFUL_PROGRAMMABLE_SWITCH = "00000088-0000-1000-8000-0026BB765291"
    STATELESS_PROGRAMMABLE_SWITCH = "00000089-0000-1000-8000-0026BB765291"
    SWITCH = "00000049-0000-1000-8000-0026BB765291"
    TARGET_CONTROL = "00000125-0000-1000-8000-0026BB765291"
    TARGET_CONTROL_MANAGEMENT = "00000122-0000-1000-8000-0026BB765291"
    TELEVISION = "000000D8-0000-1000-8000-0026BB765291"
    TEMPERATURE_SENSOR = "0000008A-0000-1000-8000-0026BB765291"
    THERMOSTAT = "0000004A-0000-1000-8000-0026BB765291"
    THHREAD_TRANSPORT = "00000701-0000-1000-8000-0026BB765291"
    TIME_INFORMATION = "00000099-0000-1000-8000-0026BB765291"
    TRANSFER_TRANSPORT_MANAGEMENT = "00000203-0000-1000-8000-0026BB765291"
    TUNNEL = "00000056-0000-1000-8000-0026BB765291"
    VALVE = "000000D0-0000-1000-8000-0026BB765291"
    WINDOW = "0000008B-0000-1000-8000-0026BB765291"
    WINDOW_COVERING = "0000008C-0000-1000-8000-0026BB765291"
    WI_FI_ROUTER = "0000020A-0000-1000-8000-0026BB765291"
    WI_FI_SATELLITE = "0000020F-0000-1000-8000-0026BB765291"
    WI_FI_TRANSPORT = "0000022A-0000-1000-8000-0026BB765291"

    BASE_UUID = "-0000-1000-8000-0026BB765291"

    @staticmethod
    def get_uuid(item_name: str) -> str:
        """
        Returns the full length UUID for either a shorted UUID or textual characteristic type name. For information on
        full and short UUID consult chapter 5.6.1 page 72 of the specification. It also supports to pass through full
        HomeKit UUIDs.

        :param item_name: either the type name (e.g. "public.hap.characteristic.position.current") or the short UUID or
                          a HomeKit specific full UUID.
        :return: the full UUID (e.g. "0000006D-0000-1000-8000-0026BB765291")
        :raises KeyError: if the input is neither a short UUID nor a type name. Specific error is given in the message.
        """
        if len(item_name) == 36:
            return item_name.upper()

        if len(item_name) <= 8:
            prefix = "0" * (8 - len(item_name))
            return f"{prefix}{item_name}{ServicesTypes.BASE_UUID}"

        raise KeyError(f"{item_name} not a valid UUID or short UUID")

    @staticmethod
    def get_short_uuid(item_name: str) -> str:
        """
        Returns the short UUID for either a full UUID or textual service type name. For information on
        full and short UUID consult chapter 5.6.1 page 72 of the specification. It also supports to pass through full
        non-HomeKit UUIDs.

        :param item_name: either the type name (e.g. "public.hap.characteristic.position.current") or the short UUID as
                          string or a HomeKit specific full UUID.
        :return: the short UUID (e.g. "6D" instead of "0000006D-0000-1000-8000-0026BB765291")
        :raises KeyError: if the input is neither a UUID nor a type name. Specific error is given in the message.
        """
        if item_name.upper().endswith(ServicesTypes.BASE_UUID):
            item_name = item_name.upper()
            item_name = item_name.split("-", 1)[0]
            return item_name.lstrip("0")

        return item_name.upper()
