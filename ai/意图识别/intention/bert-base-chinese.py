import pandas as pd
import torch
from datasets import Dataset
from transformers import BertForSequenceClassification, Trainer, TrainingArguments, BertTokenizer

# 创建一个示例 DataFrame
data = {
    'text': [
        "我最近皮肤上长了很多痘痘，怎么办？",
        "我怀孕了，想了解一下产前检查。",
        "孩子最近咳嗽了好几天，应该怎么办？",
        "昨天摔了一跤，腿部剧烈疼痛。",
        "最近老是头痛，感觉有些力不从心。",
        "我的月经总是很不规律，不知道是不是有问题。",
        "孩子老是拉肚子，吃了药也不见好转。",
        "我妈妈的血糖一直很高，需要怎么控制？",
        "我发现自己有皮肤过敏的情况，不知道怎么办。",
        "我最近脖子痛，动不了，应该去哪个科看病？",
        "我的儿子最近有发热症状，好像是感冒。",
        "月经不调，有时候特别疼，是不是妇科的问题？",
        "我的小孩昨天摔了一跤，膝盖好像肿了。",
        "经常头晕，心慌，胸口不舒服，可能是什么问题？",
        "我感觉腹部很胀痛，吃什么药好？"
    ],
    'label': [
        0,  # 皮肤科问题
        1,  # 妇科问题
        2,  # 儿科问题
        3,  # 外科问题
        4,  # 内科问题
        1,  # 妇科问题
        2,  # 儿科问题
        4,  # 内科问题
        0,  # 皮肤科问题
        3,  # 外科问题
        2,  # 儿科问题
        1,  # 妇科问题
        3,  # 外科问题
        4,  # 内科问题
        4  # 内科问题
    ]  # 0: 皮肤科问题, 1: 妇科问题，2: 儿科问题、3: 外科问题，4: 内科问题
}

df = pd.DataFrame(data)

# 将 DataFrame 转换为 datasets.Dataset 对象
dataset = Dataset.from_pandas(df)

# 使用 train_test_split 将数据集划分为训练集和测试集
dataset = dataset.train_test_split(test_size=0.2)  # 80% 训练集, 20% 测试集

# 获取训练集和测试集
train_dataset = dataset['train']
test_dataset = dataset['test']

# 加载预训练模型和分词器
# model = BertForSequenceClassification.from_pretrained('bert-base-chinese', num_labels=2)
model = BertForSequenceClassification.from_pretrained('bert-base-chinese', num_labels=5)
tokenizer = BertTokenizer.from_pretrained('bert-base-chinese')


# 数据预处理函数
def preprocess_function(examples):
    return tokenizer(examples['text'], padding='max_length', truncation=True)


# 数据预处理
train_dataset = train_dataset.map(preprocess_function, batched=True)
test_dataset = test_dataset.map(preprocess_function, batched=True)

# 设置训练参数
training_args = TrainingArguments(
    output_dir='./results',  # 输出目录
    num_train_epochs=3,  # 训练周期
    per_device_train_batch_size=2,  # 每个设备的训练批量大小
    per_device_eval_batch_size=16,  # 每个设备的评估批量大小
    warmup_steps=500,  # 预热步骤数
    weight_decay=0.01,  # 权重衰减
    logging_dir='./logs',  # 日志目录
)

# 创建Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=test_dataset,
)

# 开始训练
trainer.train()

# 评估模型
eval_results = trainer.evaluate()

# 打印评估结果
print("评估结果：", eval_results)

# 输入文本
input_text = "最近背部疼痛，长期坐办公室是不是造成的？"
inputs = tokenizer(input_text, return_tensors="pt")

# 将模型和输入移动到 CPU
device = torch.device('mps')  # 强制使用 CPU 设备

model.to(device)
inputs = {key: value.to(device) for key, value in inputs.items()}

# 获取模型的输出
outputs = model(**inputs)

# 获取 logits
logits = outputs.logits

# 使用 argmax 获取预测标签
predicted_label = torch.argmax(logits, dim=-1).item()

print(predicted_label)
