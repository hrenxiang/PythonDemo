import pandas as pd
import torch
from datasets import Dataset
from sklearn.metrics import accuracy_score, precision_recall_fscore_support

# 创建一个示例 DataFrame
data = {
    'text': [
        '今天是晴天',
        '今天是阴天',
        '今天是雨天',
        '今天是多云'
    ],
    'label': [
        2, 2, 2, 2
    ]  # 0: 问题, 1: 预定
}

df = pd.DataFrame(data)

# 将 DataFrame 转换为 datasets.Dataset 对象
dataset = Dataset.from_pandas(df)

# 使用 train_test_split 将数据集划分为训练集和测试集
dataset = dataset.train_test_split(test_size=0.2)  # 80% 训练集, 20% 测试集

# 查看分割后的数据集
print(dataset)

# 获取训练集和测试集
train_dataset = dataset['train']
test_dataset = dataset['test']

# 显示训练集样本
print("训练集：")
print(train_dataset[0])

# 显示测试集样本
print("测试集：")
print(test_dataset[0])

from transformers import BertForSequenceClassification, Trainer, TrainingArguments, BertTokenizer

# 加载预训练模型和分词器
# model = BertForSequenceClassification.from_pretrained('bert-base-chinese', num_labels=2)
model = BertForSequenceClassification.from_pretrained('./results/checkpoint-12', num_labels=3)
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
    per_device_train_batch_size=4,  # 每个设备的训练批量大小
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
input_text = "今天有雨"
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
