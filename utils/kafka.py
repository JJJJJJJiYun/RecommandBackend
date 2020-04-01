from kafka import KafkaConsumer

# 使用group,对于同一个group的成员只有一个消费者实例可以读取数据
consumer = KafkaConsumer('user_action', group_id='recommand_system', bootstrap_servers=['127.0.0.1:9092'])
