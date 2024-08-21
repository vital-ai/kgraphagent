import base64
import json
import logging
from typing import Dict


class VitalSignsUtils:
    @staticmethod
    def get_object_type(objects, type_value: str):
        for obj in objects:
            if obj.get('type') == type_value:
                return obj
        return None

    @staticmethod
    def unpack_container(container):
        if container is None:
            return None
        container_string = container.get("http://vital.ai/ontology/haley-ai-question#hasSerializedContainer")
        if container_string is None:
            return None
        decoded_bytes = base64.b64decode(container_string)
        json_string = decoded_bytes.decode('utf-8')
        object_list = json.loads(json_string)
        return object_list

    @staticmethod
    def log_object_list(label: str, object_list: Dict):
        logger = logging.getLogger("HaleyAgentLogger")
        logger.info(f"-----------------\nLogging {label}:")
        for obj in object_list:
            logger.info(f"Object: {obj}")
        logger.info("-----------------")
