import re

from deepdiff import DeepDiff

changeBefore = {
    "assetType": 0,
    "baseInfoDto": {
        "assetId": 1868478527153311745,
        "assetName": "资产名称",
        "assetDescription": "资产描述",
        "assetType": "0",
        "assetTypeName": "数据资源",
        "dataSource": [
            "1"
        ],
        "dataSourceDesc": "",
        "regionScope": "0",
        "regionScopeName": "全国",
        "dataCoverageArea": [],
        "dataCoverageAreaZh": [],
        "useCase": "使用场景",
        "dataIndustry": "08",
        "dataIndustryName": "政务",
        "dataType": "0",
        "dataTypeName": "结构化数据",
        "storageType": "0",
        "storageTypeName": "数据库",
        "fileType": None,
        "fileTypeDesc": ""
    },
    "rightInfoDto": {
        "id": 1868478527262363649,
        "rightType": [
            "0",
            "1",
            "2"
        ],
        "rightTypeName": "数据资源持有权、数据加工使用权、数据产品经营权",
        "status": "2",
        "statusName": "生效中",
        "rightHolder": "91410105MA9GTY6C54",
        "rightHolderName": "黄任翔111",
        "rightHolderType": "1",
        "rightHolderTypeName": "资源持有人",
        "termType": "0",
        "termTypeName": "长期",
        "rightObtainType": "0",
        "rightObtainTypeName": "原始取得",
        "startTime": None,
        "endTime": None,
        "certificateStoragePath": None,
        "rightsScopeRestrictionsDesc": "权利范围及限制说明",
        "rightProof": [],
        "dataSourceProof": [
            {
                "fileId": "1868478344273268738",
                "fileName": "456.docx",
                "filePath": "/zzbdex-register/2024/12/16/data_source_proof/1734314926556_456.docx",
                "uploadTime": "2024-12-16 10:08:47",
                "index": None
            }
        ],
        "registrationCommitmentLetter": [
            {
                "fileId": "1868478385218064385",
                "fileName": "图片2 4@2x (1).png",
                "filePath": "/zzbdex-register/2024/12/16/commitment/1734314936318_图片2 4@2x (1).png",
                "uploadTime": "2024-12-16 10:08:56",
                "index": None
            }
        ]
    },
    "registrationList": None,
    "upperAssetList": None,
    "registrationReportList": None,
    "subAssetResourceDtoList": [
        {
            "specificInfoDto": {
                "resourceId": 1868478527346249730,
                "accessAddress": "数据库访问地址",
                "updateFrequency": "8",
                "updateFrequencyName": "年级别更新",
                "startTime": "2024-12-18 00:00:00",
                "endTime": None,
                "dataScale": 11,
                "dataScaleUnit": "0",
                "dataScaleUnitName": "条",
                "dataSampleFile": [
                    {
                        "fileId": "1868478287620804610",
                        "fileName": "新建 Microsoft Excel 工作表.xlsx",
                        "filePath": "/zzbdex-register/2024/12/16/data_sample/1734314913040_新建 Microsoft Excel 工作表.xlsx",
                        "uploadTime": "2024-12-16 10:08:33",
                        "index": None
                    }
                ],
                "tableName": "数据表名"
            },
            "metaInfoDtoList": [
                {
                    "fieldId": 1868478527514021889,
                    "fieldName": "1",
                    "fieldNameCn": "1",
                    "fieldComment": "111",
                    "fieldType": "FLOAT"
                }
            ]
        }
    ]
}

changeAfter = {
    "assetType": 0,
    "baseInfoDto": {
        "assetId": 1868478527153311745,
        "assetName": "资产名称111",
        "assetDescription": "资产描述111",
        "assetType": "0",
        "assetTypeName": "数据资源",
        "dataSource": [
            "1"
        ],
        "dataSourceDesc": "",
        "regionScope": "0",
        "regionScopeName": "全国",
        "dataCoverageArea": ["11111"],
        "dataCoverageAreaZh": ["北京"],
        "useCase": "使用场景",
        "dataIndustry": "08",
        "dataIndustryName": "政务",
        "dataType": "0",
        "dataTypeName": "结构化数据",
        "storageType": "0",
        "storageTypeName": "数据库",
        "fileType": None,
        "fileTypeDesc": ""
    },
    "rightInfoDto": {
        "id": 1868478527262363649,
        "rightType": [
            "0",
            "2"
        ],
        "rightTypeName": "数据加工使用权、数据产品经营权",
        "status": "2",
        "statusName": "生效中",
        "rightHolder": "91410105MA9GTY6C54",
        "rightHolderName": "黄任翔111",
        "rightHolderType": "1",
        "rightHolderTypeName": "资源持有人",
        "termType": "0",
        "termTypeName": "长期",
        "rightObtainType": "0",
        "rightObtainTypeName": "原始取得",
        "startTime": None,
        "endTime": None,
        "certificateStoragePath": None,
        "rightsScopeRestrictionsDesc": "权利范围及限制说明",
        "rightProof": [],
        "dataSourceProof": [
            {
                "fileId": "1868478344273268738",
                "fileName": "456.docx",
                "filePath": "/zzbdex-register/2024/12/16/data_source_proof/1734314926556_456123.docx",
                "uploadTime": "2024-12-16 10:08:47",
                "index": None
            }
        ],
        "registrationCommitmentLetter": [
            {
                "fileId": "1868478385218064385",
                "fileName": "图片2 4@2x (1).png",
                "filePath": "/zzbdex-register/2024/12/16/commitment/1734314936318_图片2 4@2x (1).png",
                "uploadTime": "2024-12-16 10:08:56",
                "index": None
            }
        ]
    },
    "registrationList": None,
    "upperAssetList": None,
    "registrationReportList": None,
    "subAssetResourceDtoList": [
        {
            "specificInfoDto": {
                "resourceId": 1868478527346249730,
                "accessAddress": "数据库访问地址111",
                "updateFrequency": "8",
                "updateFrequencyName": "年级别更新",
                "startTime": "2024-11-18 00:00:00",
                "endTime": None,
                "dataScale": 11,
                "dataScaleUnit": "0",
                "dataScaleUnitName": "条",
                "dataSampleFile": [
                    {
                        "fileId": "1868478287620804610",
                        "fileName": "新建 Microsoft Excel 工作表.xlsx",
                        "filePath": "/zzbdex-register/2024/12/16/data_sample/1734314913040_新建 Microsoft Excel 工作表.xlsx",
                        "uploadTime": "2024-12-16 10:08:33",
                        "index": None
                    }
                ],
                "tableName": "数据表名"
            },
            "metaInfoDtoList": [
                {
                    "fieldId": 1868478527514021889,
                    "fieldName": "1",
                    "fieldNameCn": "1",
                    "fieldComment": "111",
                    "fieldType": "FLOAT"
                }
            ]
        }
    ]
}

diff = DeepDiff(changeBefore, changeAfter)


# print(diff)


# 处理 values_changed
def process_values_changed(values_changed):
    result = []
    for path, change in values_changed.items():
        field_info = {
            "field": path,
            "old_value": change['old_value'],
            "new_value": change['new_value']
        }
        result.append(field_info)
    return result


# 处理 iterable_item_added
def process_items_added(iterable_item_added):
    result = []
    for path, new_item in iterable_item_added.items():
        item_info = {
            "path": path,
            "added_value": new_item
        }
        result.append(item_info)
    return result


# 处理 iterable_item_removed
def process_items_removed(iterable_item_removed):
    result = []
    for path, removed_item in iterable_item_removed.items():
        item_info = {
            "path": path,
            "removed_value": removed_item
        }
        result.append(item_info)
    return result


# 整理所有差异数据
def process_diff(diff):
    result = {
        "values_changed": process_values_changed(diff.get("values_changed", {})),
        "items_added": process_items_added(diff.get("iterable_item_added", {})),
        "items_removed": process_items_removed(diff.get("iterable_item_removed", {}))
    }
    return result


# 处理差异并输出
formatted_diff = process_diff(diff)

# 打印整理后的差异数据
import json

dumps = json.dumps(formatted_diff, ensure_ascii=False, indent=4)
print(dumps)


# 解析路径
def get_value_from_path(data, path):
    # 移除根路径部分 root，取出 key 列表
    path = re.sub(r"^root", "", path)  # 去除 'root'
    keys = re.findall(r"\['(.*?)']", path)  # 提取路径中的所有键
    keys = [key for key in keys if key]  # 去除空字符串

    value = data
    for key in keys:
        if value is None:
            return None  # 如果值为 None，则返回 None
        if isinstance(value, list):
            # 如果是列表，尝试将路径中的数字索引作为访问
            try:
                key = int(key)  # 转换为整数索引
                value = value[key]  # 通过索引访问列表
            except (ValueError, IndexError):
                return None  # 如果索引无效，返回 None
        else:
            value = value.get(key)  # 获取字典的值
    return value


# 测试路径访问
path = "root['baseInfoDto']['assetName']"
value = get_value_from_path(dumps, path)
print(f"Value at {path}: {value}")
