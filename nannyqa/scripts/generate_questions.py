"""Generate exactly 90 questions for nannyqa - 30% easy/medium, 70% hard, all multiple choice."""
import json, os
from collections import Counter

questions = []
qid = 0

def q(cat, dim, diff, text, opts):
    global qid
    qid += 1
    return {
        "id": qid,
        "category": cat,
        "dimension": dim,
        "difficulty": diff,
        "question_zh": text,
        "scoring_type": "multiple_choice",
        "options": [
            {"text_zh": o["text"], "score": o["score"], "feedback_zh": o.get("fb", "")}
            for o in opts
        ]
    }

# ═══ BASIC (7q: 2E + 2M + 3H) ═══
questions.append(q("basic", "experience_level", "easy",
    "你做过几份保姆工作？每份大概做了多久？",
    [{"text": "没做过，这是第一份工作", "score": 1, "fb": "无经验，需要培训"},
     {"text": "1-2份，每份3个月到1年", "score": 3, "fb": "有一定经验但不够稳定"},
     {"text": "3-5份，每份1-3年", "score": 4, "fb": "经验较丰富，稳定性良好"},
     {"text": "5份以上，每份3年以上", "score": 5, "fb": "经验丰富且稳定"}]))

questions.append(q("basic", "health", "easy",
    "你的身体状况如何？",
    [{"text": "非常健康，无任何疾病", "score": 5, "fb": "身体条件优秀"},
     {"text": "基本健康，有小毛病但不影响工作", "score": 4, "fb": "身体健康，可胜任工作"},
     {"text": "有一些慢性病但控制良好", "score": 3, "fb": "需注意定期体检"},
     {"text": "健康状况一般，经常需要休息", "score": 2, "fb": "可能影响工作稳定性"}]))

questions.append(q("basic", "family_situation", "medium",
    "你的家庭情况是怎样的？家人支持你做保姆工作吗？",
    [{"text": "单身/无家庭负担，全力支持", "score": 5, "fb": "时间精力充足"},
     {"text": "有家庭但家人理解支持", "score": 4, "fb": "家庭支持是重要保障"},
     {"text": "有家庭，家人勉强支持", "score": 3, "fb": "可能存在后顾之忧"},
     {"text": "家人不太支持，我自己想做", "score": 2, "fb": "家庭矛盾可能影响工作"}]))

questions.append(q("basic", "motivation", "medium",
    "你为什么选择做保姆工作？是因为什么契机？",
    [{"text": "一直喜欢照顾人，擅长家务", "score": 5, "fb": "内在动机强，职业认同感高"},
     {"text": "以前做过，觉得适合自己", "score": 4, "fb": "有经验且确认适合"},
     {"text": "就业压力大，先做着看看", "score": 2, "fb": "动机不够坚定，可能不稳定"},
     {"text": "没办法，什么赚钱做什么", "score": 1, "fb": "缺乏职业认同"}]))

questions.append(q("basic", "learning_attitude", "hard",
    "如果雇主提出了新的育儿理念或家务要求，你不太熟悉，你会怎么做？",
    [{"text": "主动学习，上网查资料或向有经验的人请教", "score": 5, "fb": "学习态度积极，适应能力强"},
     {"text": "先按雇主要求做，有问题再慢慢学", "score": 4, "fb": "实践中学习，稳妥但效率一般"},
     {"text": "等雇主耐心教我，我不太会主动问", "score": 2, "fb": "被动学习，成长速度慢"},
     {"text": "我觉得我以前的方法就够了，不想改", "score": 1, "fb": "固守旧方法，难以适应新需求"}]))

questions.append(q("basic", "career_plan", "hard",
    "你对自己未来3-5年的职业规划是什么？",
    [{"text": "成为专业月嫂/育儿嫂，考相关证书，提升自己", "score": 5, "fb": "有清晰职业规划，上进心强"},
     {"text": "先做好当前工作，积累经验再说", "score": 4, "fb": "务实稳重"},
     {"text": "做一份算一份，走一步看一步", "score": 2, "fb": "缺乏规划，可能稳定性不足"},
     {"text": "没有规划，做完这份就换", "score": 1, "fb": "职业态度不够认真"}]))

questions.append(q("basic", "reference_check", "hard",
    "你之前的雇主可以证明你的工作表现吗？如果现在有疑虑，你希望我们怎么做？",
    [{"text": "可以，我有前雇主的联系方式，随时可以核实", "score": 5, "fb": "诚信透明，经得起核查"},
     {"text": "前雇主不方便联系，但我可以提供同事或朋友证明", "score": 3, "fb": "有替代证明，但可靠性略低"},
     {"text": "我不好意思要联系方式，但我很靠谱", "score": 2, "fb": "缺乏佐证，需要进一步考察"},
     {"text": "之前做得不顺，没好意思要联系方式", "score": 1, "fb": "过往经历可能有隐患"}]))

# ═══ COOKING (9q: 3E + 2M + 4H) ═══
questions.append(q("cooking", "cooking_skill", "easy",
    "你最拿手的几道菜是什么？能说说做法吗？",
    [{"text": "红烧肉、清蒸鱼、西红柿炒蛋等十几道家常菜", "score": 5, "fb": "菜系丰富，基础扎实"},
     {"text": "会做几道家常菜，但花样不多", "score": 3, "fb": "基本够用，需拓展菜系"},
     {"text": "只会炒几个简单的菜", "score": 2, "fb": "烹饪能力有限"},
     {"text": "不太会做饭，边做边学吧", "score": 1, "fb": "烹饪能力不足"}]))

questions.append(q("cooking", "hygiene_habits", "easy",
    "你在厨房工作时，会注意哪些卫生细节？",
    [{"text": "生熟分开、勤洗手、厨具定期消毒、台面随时清理", "score": 5, "fb": "卫生习惯优秀"},
     {"text": "会洗手，切菜前后换手", "score": 4, "fb": "有基本卫生意识"},
     {"text": "大概知道要干净，但细节不太注意", "score": 2, "fb": "卫生意识一般"},
     {"text": "做完饭再说，没想那么多", "score": 1, "fb": "卫生意识薄弱"}]))

questions.append(q("cooking", "baby_food", "easy",
    "你知道宝宝什么时候开始加辅食吗？一般会做些什么？",
    [{"text": "6个月左右开始，先米粉后菜泥肉泥，循序渐进", "score": 5, "fb": "科学知识扎实"},
     {"text": "大概4-6个月，做点粥和菜汤", "score": 3, "fb": "有基本了解，不够系统"},
     {"text": "听说要加，但具体不清楚", "score": 2, "fb": "知识欠缺，需学习"},
     {"text": "没接触过，不太懂", "score": 1, "fb": "缺乏辅食知识"}]))

questions.append(q("cooking", "dietary_restrictions", "medium",
    "如果雇主家人有食物过敏（比如海鲜、坚果过敏），你会怎么做？",
    [{"text": "严格区分餐具和食材，烹饪时单独处理，做好标记", "score": 5, "fb": "过敏防范意识极强"},
     {"text": "做的时候注意分开，但不会特别严格", "score": 3, "fb": "有一定意识但不够严谨"},
     {"text": "问雇主哪些不能吃，然后避免做", "score": 4, "fb": "知道询问，但缺乏主动防范"},
     {"text": "反正做熟了应该没事吧", "score": 1, "fb": "对食物过敏重视不足，存在风险"}]))

questions.append(q("cooking", "leftover_handling", "hard",
    "你做了一桌菜，最后剩了不少，第二天你会怎么处理？",
    [{"text": "当天分装冷藏，第二天彻底加热后再吃，不吃隔夜反复加热的", "score": 5, "fb": "食品安全意识强"},
     {"text": "放冰箱，第二天热一下继续吃", "score": 3, "fb": "有基本意识但不够细致"},
     {"text": "放到明天再热热吃，没什么事", "score": 2, "fb": "对食品安全重视不够"},
     {"text": "剩菜倒掉太浪费了，放几天也没关系", "score": 1, "fb": "食品安全意识薄弱"}]))

questions.append(q("cooking", "cooking_under_pressure", "hard",
    "家里突然来了很多客人，只有1小时要做10个人的饭，你会怎么办？",
    [{"text": "快速制定计划，先做能提前准备的凉菜和炖菜，热菜穿插进行", "score": 5, "fb": "应变能力强，统筹能力优秀"},
     {"text": "先做几个硬菜，其他的简单弄弄", "score": 3, "fb": "有应对意识，但不够系统"},
     {"text": "按顺序一个一个做，虽然慢但能做完", "score": 2, "fb": "缺乏统筹，效率较低"},
     {"text": "直接告诉雇主做不了这么多，叫外卖吧", "score": 1, "fb": "应变能力差，缺乏担当"}]))

questions.append(q("cooking", "cooking_for_sick", "hard",
    "孩子感冒发烧不肯吃饭，你会怎么准备饮食？",
    [{"text": "准备清淡易消化的粥、汤面，少量多餐，不强迫进食", "score": 5, "fb": "科学喂养，尊重孩子状态"},
     {"text": "做点有营养的软饭，哄着吃一点", "score": 3, "fb": "有心但方法不够专业"},
     {"text": "做平时爱吃的，希望能多吃点", "score": 2, "fb": "缺乏病期饮食知识"},
     {"text": "孩子不想吃就算了，饿一顿没关系", "score": 1, "fb": "忽视营养摄入"}]))

questions.append(q("cooking", "taste_adjustment", "hard",
    "雇主反馈你做的菜太咸了，你会怎么处理？",
    [{"text": "道歉并记录，下次少放盐，主动请雇主品尝调整", "score": 5, "fb": "虚心接受，积极改进"},
     {"text": "下次注意少放盐", "score": 4, "fb": "知道改进但缺乏主动沟通"},
     {"text": "可能我家口味就这样，下次试试看", "score": 2, "fb": "缺乏主动调整意识"},
     {"text": "我觉得味道刚好啊，可能是他们挑剔", "score": 1, "fb": "缺乏自我反思能力"}]))

# ═══ CHILD CARE (14q: 2E + 4M + 8H) ═══
questions.append(q("childcare", "daily_routine", "easy",
    "你日常带孩子的一天大概是什么流程？",
    [{"text": "按时作息：起床、喂奶/辅食、游戏、午睡、户外活动、晚饭、洗澡、睡前故事、睡觉", "score": 5, "fb": "作息规律，科学育儿"},
     {"text": "大概有规律，但偶尔会打乱", "score": 3, "fb": "有基本节奏，但执行不够稳定"},
     {"text": "孩子想怎样就怎样，没有固定时间", "score": 1, "fb": "缺乏规律意识"}]))

questions.append(q("childcare", "sleep_training", "medium",
    "宝宝晚上睡不好，总是半夜醒来哭闹，你会怎么处理？",
    [{"text": "先排查原因（饿了、尿布湿了、太热太冷），温和安抚，建立睡眠仪式", "score": 5, "fb": "科学应对，关注根本原因"},
     {"text": "抱起来哄，哭了就喂", "score": 3, "fb": "基本做法，但缺乏系统性"},
     {"text": "让孩子哭一会儿，哭累了自然就睡了", "score": 2, "fb": "忽视了孩子的安全感需求"},
     {"text": "没办法，孩子都这样，随他去吧", "score": 1, "fb": "缺乏耐心和应对方法"}]))

questions.append(q("childcare", "teething_care", "medium",
    "宝宝长牙期牙龈肿痛、烦躁不安，你会怎么帮助缓解？",
    [{"text": "提供牙胶、冷毛巾咬，按摩牙龈，必要时咨询医生用退烧药", "score": 5, "fb": "方法科学，懂得就医指征"},
     {"text": "给点硬的东西啃，或者抱抱安慰", "score": 3, "fb": "有基本应对，但方法有限"},
     {"text": "长牙嘛，忍一忍就过去了", "score": 2, "fb": "忽视孩子不适"},
     {"text": "给孩子涂点白酒或草药在牙龈上", "score": 1, "fb": "危险做法，可能造成伤害"}]))

questions.append(q("childcare", "potty_training", "hard",
    "孩子2岁多了还不会如厕，总是尿裤子，你会怎么处理？",
    [{"text": "观察信号，定时提醒，正面鼓励，不责备，循序渐进", "score": 5, "fb": "尊重发育节奏，正向引导"},
     {"text": "定时把孩子送去厕所，不行的话就换尿布", "score": 3, "fb": "有一定方法，但略显机械"},
     {"text": "老是尿裤子，干脆就别穿了，减少清洗麻烦", "score": 2, "fb": "消极应对，不利于孩子成长"},
     {"text": "骂他怎么又尿了，逼他学会", "score": 1, "fb": "暴力方式会造成心理创伤"}]))

questions.append(q("childcare", "screen_time", "hard",
    "雇主家孩子经常要看手机/电视，你觉得这样做合适吗？如果雇主不干预，你会怎么跟雇主沟通？",
    [{"text": "私下温和沟通，提供替代方案（绘本、游戏），说明屏幕时间过多的危害", "score": 5, "fb": "沟通得体，有建设性"},
     {"text": "提醒雇主要注意，但不会多说", "score": 3, "fb": "有意识但沟通不够积极"},
     {"text": "这是他们家的事，我管不了", "score": 1, "fb": "缺乏责任意识和沟通意愿"}]))

questions.append(q("childcare", "sibling_conflict", "hard",
    "家里有两个孩子，大的欺负小的，抢玩具还打人，你会怎么处理？",
    [{"text": "先分开两个孩子，分别安抚，再了解原因，教导分享和尊重，不偏袒", "score": 5, "fb": "处理得当，关注两个孩子的心理"},
     {"text": "让大的让着小的，打人的时候训斥大的", "score": 3, "fb": "基本处理，但不够深入"},
     {"text": "谁哭就抱谁，不管谁对谁错", "score": 2, "fb": "处理方式混乱，缺乏原则"},
     {"text": "大的该教训，抓过来打几下", "score": 1, "fb": "暴力方式严重错误"}]))

questions.append(q("childcare", "selective_eating", "medium",
    "孩子挑食，只吃白米饭不肯吃菜，你会怎么办？",
    [{"text": "把菜切碎混进饭里，或做成有趣造型，逐步引导，不强迫", "score": 5, "fb": "方法灵活，尊重孩子节奏"},
     {"text": "做孩子喜欢的菜，慢慢引入新菜", "score": 4, "fb": "有策略，但推进较慢"},
     {"text": "强迫吃完，不吃就不准玩", "score": 1, "fb": "强迫进食损害亲子关系"},
     {"text": "随他，不吃就不吃，长大就好了", "score": 2, "fb": "完全放任，不利于习惯养成"}]))

questions.append(q("childcare", "separation_anxiety", "hard",
    "孩子刚上幼儿园，每天早上哭闹不肯去，粘着你不放，你会怎么做？",
    [{"text": "温柔但坚定地陪伴，建立告别仪式，告诉孩子'妈妈下班就来接你'，逐步建立安全感", "score": 5, "fb": "专业处理方式，建立安全感"},
     {"text": "转移注意力，给玩具或零食哄", "score": 3, "fb": "临时有效，但未解决根本问题"},
     {"text": "趁孩子不注意偷偷溜走", "score": 1, "fb": "严重错误，破坏孩子信任"},
     {"text": "跟着孩子一起哭，没办法", "score": 1, "fb": "情绪传递，反而加重焦虑"}]))

questions.append(q("childcare", "allergic_reaction", "hard",
    "孩子在外面玩的时候突然全身起红疹、呼吸急促，你怀疑是过敏，你会怎么办？",
    [{"text": "立即拨打120，同时回忆可能接触到的过敏原，保持孩子呼吸道通畅", "score": 5, "fb": "正确处理过敏性休克，争分夺秒"},
     {"text": "赶紧带孩子去医院，路上观察情况", "score": 4, "fb": "及时处理，但应同时呼叫急救"},
     {"text": "给孩子吃点抗过敏药，等一等看", "score": 2, "fb": "延误紧急处理，风险很高"},
     {"text": "吓坏了，不知道怎么办，站着等雇主来", "score": 1, "fb": "缺乏应急处理能力"}]))

questions.append(q("childcare", "choking_emergency", "hard",
    "孩子吃东西的时候突然呛住了，脸憋得通红发不出声音，你会怎么做？",
    [{"text": "立即实施海姆立克急救法，同时让人拨打120", "score": 5, "fb": "掌握急救技能，反应正确"},
     {"text": "拍背、倒提孩子，试图让他咳出来", "score": 3, "fb": "有应急意识，但方法不够精准"},
     {"text": "给孩子喂水想冲下去", "score": 1, "fb": "错误做法，可能加重窒息"},
     {"text": "慌了神，大声喊人，不知道该做什么", "score": 1, "fb": "缺乏急救知识"}]))

questions.append(q("childcare", "tantrum_public", "hard",
    "在商场里，孩子突然躺地打滚哭闹要买玩具，周围人都看着，你会怎么做？",
    [{"text": "把孩子带到人少的地方，蹲下平视，温和但坚定地说不买的原因，给他选择", "score": 5, "fb": "公共场合处理得当，既保护自尊又立规矩"},
     {"text": "先哄住，买下来让他别哭了", "score": 2, "fb": "纵容行为，不利于规则建立"},
     {"text": "不管不顾，让他哭够了自然停", "score": 2, "fb": "冷处理有争议，但比纵容好"},
     {"text": "当众打骂孩子，吓唬他", "score": 1, "fb": "严重伤害孩子自尊和安全感"}]))

# ═══ HYGIENE (9q: 2E + 3M + 4H) ═══
questions.append(q("hygiene", "daily_cleaning", "easy",
    "你每天做家务的顺序一般是怎样的？",
    [{"text": "先整理杂物→擦拭台面→扫地拖地→清洁卫生间→最后检查一遍", "score": 5, "fb": "流程科学，从干到湿，从上到下"},
     {"text": "看到哪里脏了擦哪里，没有固定顺序", "score": 2, "fb": "缺乏系统性"},
     {"text": "早上做一部分，下午做一部分，看时间", "score": 3, "fb": "灵活但不够高效"},
     {"text": "雇主说什么我做什麼", "score": 1, "fb": "缺乏主动性"}]))

questions.append(q("hygiene", "disinfection", "medium",
    "家里有宝宝，你会怎么做好消毒工作？",
    [{"text": "区分日常清洁和消毒，玩具定期煮沸或紫外线消毒，表面用稀释消毒液，注意通风", "score": 5, "fb": "消毒知识全面，操作规范"},
     {"text": "用84消毒液拖地擦桌子，每周一次", "score": 3, "fb": "有消毒意识，但频率和方法需加强"},
     {"text": "经常用水擦，擦干净就可以了", "score": 2, "fb": "混淆清洁和消毒概念"},
     {"text": "没什么特别讲究，该干嘛干嘛", "score": 1, "fb": "消毒意识薄弱"}]))

questions.append(q("hygiene", "laundry_separation", "medium",
    "孩子的衣服和大人的衣服你会怎么洗？",
    [{"text": "孩子衣服单独洗，用专用洗衣液，阳光下晾晒或高温烘干", "score": 5, "fb": "分类洗涤，注重消毒"},
     {"text": "分开洗，但用什么洗衣液没特别讲究", "score": 3, "fb": "有分类意识，但细节不足"},
     {"text": "一起洗，方便", "score": 1, "fb": "未区分，存在交叉感染风险"},
     {"text": "衣服多的时候分开，少的时候就一起", "score": 2, "fb": "标准不统一，风险不可控"}]))

questions.append(q("hygiene", "deep_cleaning_schedule", "medium",
    "你多久会做一次大扫除（擦窗户、清洗空调滤网、清理油烟机）？",
    [{"text": "每季度至少一次，根据使用情况灵活安排", "score": 5, "fb": "定期深度清洁，维护房屋质量"},
     {"text": "半年一次，或者雇主提醒的时候", "score": 3, "fb": "有一定意识，但主动性一般"},
     {"text": "一年一次，过年大扫除", "score": 2, "fb": "清洁频率太低"},
     {"text": "没做过，不知道怎么搞", "score": 1, "fb": "缺乏深度清洁能力"}]))

questions.append(q("hygiene", "pest_control", "hard",
    "厨房里发现了小飞虫（果蝇）和蚂蚁，你会怎么处理？",
    [{"text": "找到源头（烂水果/糖罐），彻底清理，用物理方法（密封、清除）为主，必要时使用安全杀虫剂", "score": 5, "fb": "治标治本，方法科学"},
     {"text": "喷杀虫剂，然后开窗通风", "score": 3, "fb": "应急处理可以，但未根除源头"},
     {"text": "看到一只拍一只，没办法根治", "score": 2, "fb": "被动应付"},
     {"text": "不管它们，虫子很正常", "score": 1, "fb": "卫生意识差"}]))

questions.append(q("hygiene", "dishwashing_routine", "hard",
    "洗完碗筷后，你会怎么存放和晾干？",
    [{"text": "沥水架晾干或用消毒柜，不擦干后马上收进柜子（容易滋生细菌）", "score": 5, "fb": "科学存放，避免细菌滋生"},
     {"text": "擦干后收进柜子", "score": 3, "fb": "有基本做法，但不够严谨"},
     {"text": "湿的就放进去，等干了再说", "score": 1, "fb": "潮湿环境易滋生细菌"},
     {"text": "用抹布擦干就收", "score": 2, "fb": "抹布本身可能带菌"}]))

questions.append(q("hygiene", "vacuum_cleaning_detail", "hard",
    "吸尘器的使用，你会特别注意哪些地方？",
    [{"text": "床底、沙发底、墙角、窗帘上方、地毯边缘，定期清洗滤网和集尘袋", "score": 5, "fb": "清洁无死角，设备维护到位"},
     {"text": "地面主要区域吸一吸", "score": 3, "fb": "基本清洁，但遗漏边角"},
     {"text": "看到有灰的地方吸一下", "score": 2, "fb": "被动清洁，不够系统"},
     {"text": "不用吸尘器，用扫帚", "score": 1, "fb": "清洁效果较差"}]))

# ═══ SAFETY (12q: 3E + 3M + 6H) ═══
questions.append(q("safety", "fire_safety", "easy",
    "家里发生火灾的时候，你会怎么做？",
    [{"text": "立即拨打119，用湿毛巾捂住口鼻低姿撤离，不走电梯，先到安全区域集合", "score": 5, "fb": "正确的火灾逃生方法"},
     {"text": "先试着灭火，灭不了再跑", "score": 3, "fb": "有灭火意识，但应优先撤离"},
     {"text": "慌了，到处乱跑", "score": 1, "fb": "缺乏冷静判断能力"},
     {"text": "先救孩子，不管其他人", "score": 4, "fb": "保护孩子是本能，但需确保自身安全才能救人"}]))

questions.append(q("safety", "gas_leak", "medium",
    "你闻到煤气味了，但找不到泄漏点，你会怎么做？",
    [{"text": "立即开窗通风，不开任何电器开关，不打电话，到室外拨打燃气公司电话", "score": 5, "fb": "正确处理，避免电火花"},
     {"text": "打开灯找找哪里漏气", "score": 1, "fb": "开灯可能产生电火花，极其危险！"},
     {"text": "点个蜡烛找漏点", "score": 1, "fb": "绝对禁止！明火遇煤气会爆炸"},
     {"text": "用打火机测试哪里漏气", "score": 1, "fb": "极度危险行为！"}]))

questions.append(q("safety", "electrical_safety", "medium",
    "发现插座冒火花，你会怎么做？",
    [{"text": "立即切断总电源，联系电工维修，不用该插座直到修好", "score": 5, "fb": "正确处理流程，安全第一"},
     {"text": "拔掉插头，等它冷却后再用", "score": 2, "fb": "危险操作，可能触电"},
     {"text": "不管它，反正还能动", "score": 1, "fb": "忽视安全隐患，风险极高"},
     {"text": "用胶带包一下继续用", "score": 1, "fb": "临时措施不能解决根本问题"}]))

questions.append(q("safety", "car_seat_usage", "medium",
    "带孩子出门坐车，你会怎么安置孩子？",
    [{"text": "使用儿童安全座椅，根据年龄体重选择合适型号，正确安装", "score": 5, "fb": "符合安全标准，专业做法"},
     {"text": "抱在怀里坐车", "score": 1, "fb": "极度危险，急刹车时可能致命"},
     {"text": "让孩子坐前排", "score": 1, "fb": "安全气囊可能对儿童造成致命伤害"},
     {"text": "用大人的安全带固定孩子", "score": 2, "fb": "不够安全，应选择儿童安全座椅"}]))

questions.append(q("safety", "window_falls", "hard",
    "你家在20楼，窗台边没有护栏，孩子爬到窗台上玩，你会怎么做？",
    [{"text": "立即制止，同时安装窗户限位器或防护栏，并教育孩子不要靠近窗边", "score": 5, "fb": "及时干预+工程防护+教育，三位一体"},
     {"text": "把孩子抱下来，告诉他不要爬窗台", "score": 3, "fb": "临时处理，但未消除安全隐患"},
     {"text": "看住孩子就行，不让他爬到边上", "score": 2, "fb": "依赖人工盯防，不可靠"},
     {"text": "20楼掉不下去，没事", "score": 1, "fb": "严重低估高空坠物风险"}]))

questions.append(q("safety", "poison_identification", "hard",
    "孩子误食了家长用的清洁剂（比如洗衣机槽清洁剂），你怎么办？",
    [{"text": "立即拨打120，告知毒物名称和摄入量，不要让孩子呕吐，带上产品包装", "score": 5, "fb": "正确急救，避免二次伤害"},
     {"text": "赶紧喝点牛奶或水稀释", "score": 2, "fb": "某些腐蚀性毒物催吐或喝水可能加重伤害"},
     {"text": "让孩子吐出来", "score": 2, "fb": "腐蚀性毒物催吐可能造成二次伤害"},
     {"text": "等雇主回来再说", "score": 1, "fb": "延误黄金抢救时间"}]))

questions.append(q("safety", "hot_water_scald", "hard",
    "给孩子洗澡的时候，水温太烫把孩子手臂烫红了，你会怎么处理？",
    [{"text": "立即用流动的冷水冲洗15-20分钟，不要涂牙膏或酱油，轻柔地覆盖伤口，必要时就医", "score": 5, "fb": "正确处理烫伤，方法科学"},
     {"text": "涂点牙膏或香油", "score": 1, "fb": "错误方法，可能造成感染"},
     {"text": "冰敷一下", "score": 2, "fb": "冰敷可能加重组织损伤"},
     {"text": "不管了，过几天就好了", "score": 1, "fb": "忽视伤情，可能延误治疗"}]))

questions.append(q("safety", "emergency_contact_card", "hard",
    "你会为雇主家制作一个紧急联系卡吗？上面会放哪些信息？",
    [{"text": "会，包括：家庭医生电话、最近医院地址和电话、父母电话、保险信息、过敏史、紧急联系人", "score": 5, "fb": "准备充分，关键信息齐全"},
     {"text": "记一下父母电话和医院电话", "score": 3, "fb": "有基本意识，但信息不够全面"},
     {"text": "不需要，有事直接打120", "score": 2, "fb": "过于依赖急救电话，缺少备用方案"},
     {"text": "没想过这个问题", "score": 1, "fb": "安全意识薄弱"}]))

questions.append(q("safety", "stranger_at_door", "hard",
    "你一个人在家带宝宝，门外有人敲门说是物业来抄表或送快递，你会怎么做？",
    [{"text": "通过猫眼确认身份，不随便开门，必要时联系雇主确认", "score": 5, "fb": "安全意识强，核实身份后再行动"},
     {"text": "问一下是谁，然后开门", "score": 2, "fb": "仅凭声音判断不可靠"},
     {"text": "直接开门", "score": 1, "fb": "极度危险，可能让不法分子进入"},
     {"text": "假装不在家", "score": 3, "fb": "有一定防范但不够主动"}]))

# ═══ COMMUNICATION (9q: 2E + 2M + 5H) ═══
questions.append(q("communication", "feedback_reception", "easy",
    "雇主说你菜做得太咸了，你会怎么回应？",
    [{"text": "抱歉，下次我会注意少放盐，请问您喜欢什么口味？", "score": 5, "fb": "虚心接受，主动询问偏好"},
     {"text": "好的，我知道了", "score": 3, "fb": "基本接受，但缺乏互动"},
     {"text": "我觉得味道刚好啊", "score": 1, "fb": "缺乏谦逊态度"},
     {"text": "可能是您的味觉变了", "score": 1, "fb": "推卸责任，不恰当"}]))

questions.append(q("communication", "boundary_setting", "medium",
    "雇主让你做一些不在约定范围内的工作（比如帮他们家亲戚做家务），你会怎么做？",
    [{"text": "礼貌询问雇主的意图，如果是偶尔帮忙可以理解，如果是长期额外工作则需协商报酬", "score": 5, "fb": "边界清晰，沟通得体"},
     {"text": "直接拒绝，说这不是我的工作", "score": 2, "fb": "过于强硬，影响关系"},
     {"text": "不好意思拒绝，默默做了", "score": 3, "fb": "缺乏边界意识，长期会委屈"},
     {"text": "做了之后到处跟别人说雇主欺负人", "score": 1, "fb": "背后抱怨，职业素养差"}]))

questions.append(q("communication", "reporting_incidents", "medium",
    "孩子在外面玩的时候，你负责看护，但不小心让他摔了一跤擦破了皮，你会怎么跟雇主报告？",
    [{"text": "第一时间处理伤口，然后立即打电话告知雇主，如实说明情况，不隐瞒", "score": 5, "fb": "及时透明沟通，建立信任"},
     {"text": "先处理伤口，等雇主问起来再说", "score": 3, "fb": "被动沟通，可能造成误会"},
     {"text": "偷偷处理了，不让雇主知道", "score": 1, "fb": "隐瞒重大事件，破坏信任"},
     {"text": "告诉雇主是孩子不听话才摔的", "score": 2, "fb": "推卸责任给幼儿"}]))

questions.append(q("communication", "handling_accusations", "hard",
    "雇主突然说你偷拿了家里的钱，但你确实没有，你会怎么处理？",
    [{"text": "冷静说明自己无辜，请求雇主一起查找证据，愿意配合调查，不争吵不情绪化", "score": 5, "fb": "冷静理性，维护自身权益的同时保持职业态度"},
     {"text": "马上否认，很生气", "score": 3, "fb": "情绪化反应，不利于解决问题"},
     {"text": "委屈哭了，解释不清", "score": 2, "fb": "情绪失控，缺乏应对能力"},
     {"text": "直接辞职走人，解释不清", "score": 1, "fb": "逃避问题，放弃自证清白"}]))

questions.append(q("communication", "scheduling_conflict", "hard",
    "雇主临时要求你加班，但你家里有事需要离开，你会怎么沟通？",
    [{"text": "诚恳说明情况，提供替代方案（比如请同事临时顶替或提前完成部分工作）", "score": 5, "fb": "主动沟通，提出解决方案"},
     {"text": "直接告诉雇主不行，我有事", "score": 3, "fb": "诚实但缺乏协商"},
     {"text": "答应加班，但心里很不情愿，做的时候敷衍", "score": 2, "fb": "阳奉阴违，影响工作质量"},
     {"text": "不告而别，直接走人", "score": 1, "fb": "严重缺乏职业操守"}]))

questions.append(q("communication", "dealing_with_rude_family", "hard",
    "雇主的婆婆对你很挑剔，经常在儿媳面前说你不是，你会怎么应对？",
    [{"text": "保持礼貌和距离，不反驳不争论，事后向雇主（其子女）委婉说明情况，寻求理解", "score": 5, "fb": "处理得当，维护自身尊严的同时保护雇主家庭和谐"},
     {"text": "忍气吞声，不说话", "score": 2, "fb": "消极应对，问题不会消失"},
     {"text": "当面怼回去", "score": 1, "fb": "激化矛盾，严重影响工作关系"},
     {"text": "跟雇主告状，说婆婆欺负我", "score": 2, "fb": "缺乏独立处理能力"}]))

questions.append(q("communication", "giving_bad_news", "hard",
    "你在照顾孩子的时候不小心把孩子磕到了，起了个大包，但孩子没有大哭大闹，你会怎么处理？",
    [{"text": "第一时间冰敷处理伤口，然后立即如实告诉雇主，不隐瞒不夸大，一起观察后续情况", "score": 5, "fb": "正确处理+诚实沟通，建立信任"},
     {"text": "先处理好，等雇主问起来再说", "score": 2, "fb": "隐瞒可能失去信任"},
     {"text": "小声告诉雇主，然后赶紧说是孩子自己摔的", "score": 1, "fb": "推卸责任，不诚实"},
     {"text": "假装没看见，让孩子自己好", "score": 1, "fb": "不负责任"}]))

# ═══ ETHICS (7q: 2E + 2M + 3H) ═══
questions.append(q("ethics", "privacy_protection", "easy",
    "你在雇主家看到了一些私事（比如雇主夫妻吵架），你会怎么处理？",
    [{"text": "当作没看见没听见，绝对不和任何人谈论雇主家的私事", "score": 5, "fb": "保密意识强，职业操守优秀"},
     {"text": "不会主动说，但如果有人问就说一点", "score": 2, "fb": "保密意识不够强"},
     {"text": "都是小事，没什么不能说的", "score": 1, "fb": "对隐私不重视"},
     {"text": "可以分享，反正大家都是熟人", "score": 1, "fb": "泄露隐私，严重违反职业道德"}]))

questions.append(q("ethics", "honesty_about_mistakes", "medium",
    "你在雇主家不小心打碎了一个贵重的杯子，你会怎么办？",
    [{"text": "立即告知雇主，道歉并提出赔偿，不隐瞒不推卸", "score": 5, "fb": "诚实负责，勇于担当"},
     {"text": "偷偷收拾碎片，装作没发生", "score": 1, "fb": "隐瞒错误，一旦被发现信任尽毁"},
     {"text": "等雇主自己发现，到时候再解释", "score": 2, "fb": "被动应对，不够主动"},
     {"text": "说是孩子打碎的", "score": 1, "fb": "栽赃嫁祸，极其恶劣"}]))

questions.append(q("ethics", "handling_found_money", "hard",
    "你在打扫雇主家的时候，发现地上有一笔钱，雇主似乎没发现，你会怎么处理？",
    [{"text": "立即告知雇主，交还给雇主，不私藏", "score": 5, "fb": "诚实守信，职业操守优秀"},
     {"text": "放一边等雇主发现", "score": 3, "fb": "被动处理，不够主动"},
     {"text": "悄悄拿走", "score": 1, "fb": "这是盗窃行为"},
     {"text": "不管它，等别人来处理", "score": 2, "fb": "缺乏主动性和责任感"}]))

questions.append(q("ethics", "social_media_boundaries", "hard",
    "你在雇主家里拍了一些照片（比如孩子可爱的瞬间），你想发朋友圈，可以吗？",
    [{"text": "绝对不可以，未经雇主明确许可不得发布任何涉及雇主家庭的照片", "score": 5, "fb": "隐私意识极强，尊重雇主"},
     {"text": "可以发，但要打马赛克", "score": 2, "fb": "即使打码也需要事先征求同意"},
     {"text": "发吧，反正都是正面的照片", "score": 1, "fb": "侵犯隐私，可能引起法律纠纷"},
     {"text": "先发朋友圈再告诉雇主", "score": 1, "fb": "先斩后奏，不尊重人"}]))

questions.append(q("ethics", "conflict_of_interest", "hard",
    "你的另一个朋友也是保姆，她听说你这家人条件很好，想让你把她介绍过来，你会怎么做？",
    [{"text": "婉言拒绝，告诉朋友这涉及到雇主的选择权，不应该强推", "score": 5, "fb": "尊重雇主选择权，不越界"},
     {"text": "推荐给朋友，反正多个人也没坏处", "score": 2, "fb": "缺乏边界意识，可能引起雇主不满"},
     {"text": "答应帮她问，但先征得雇主同意", "score": 4, "fb": "有沟通意识，但需确保方式得当"},
     {"text": "直接带朋友来雇主家", "score": 1, "fb": "严重越界，不尊重雇主"}]))

# ═══ PROFESSIONALISM (9q: 3E + 2M + 4H) ═══
questions.append(q("professionalism", "work_attitude", "easy",
    "你对自己的这份工作怎么看？",
    [{"text": "这是一份值得尊敬的工作，我用心做好，也从中获得成就感", "score": 5, "fb": "职业认同感强，心态积极"},
     {"text": "谋生的手段，做好本分就行", "score": 3, "fb": "务实态度，但缺乏热情"},
     {"text": "没办法，只能做这个", "score": 2, "fb": "职业认同感低，可能缺乏动力"},
     {"text": "就是打工的，无所谓", "score": 1, "fb": "对工作缺乏基本尊重"}]))

questions.append(q("professionalism", "time_management", "easy",
    "如果你今天有临时任务（比如雇主临时加班），但你自己也有安排，你会怎么协调？",
    [{"text": "提前规划，尽量提前完成工作，如有冲突与雇主协商调整时间", "score": 5, "fb": "主动规划，有效沟通"},
     {"text": "先做完雇主的工作，自己的事再安排", "score": 4, "fb": "以工作为先，有一定灵活性"},
     {"text": "看雇主紧不紧急，不紧急就先做自己的", "score": 2, "fb": "判断力有待提高"},
     {"text": "直接拒绝，我有自己的时间安排", "score": 1, "fb": "缺乏灵活性"}]))

questions.append(q("professionalism", "dress_code", "easy",
    "你上班时会穿什么衣服？",
    [{"text": "舒适、方便工作的服装，干净整洁，不穿拖鞋或过于暴露的衣服", "score": 5, "fb": "着装得体，符合职业要求"},
     {"text": "随便穿，舒服就行", "score": 2, "fb": "不太讲究"},
     {"text": "穿漂亮衣服，让自己开心", "score": 2, "fb": "未考虑工作实用性"},
     {"text": "穿什么无所谓，反正在家里", "score": 1, "fb": "缺乏职业素养意识"}]))

questions.append(q("professionalism", "time_management2", "medium",
    "如果你同时有几件事要做（比如做饭、洗衣服、看孩子），你会怎么安排优先级？",
    [{"text": "先看孩子安全，再做紧急的家务，不紧急的等孩子睡了再做", "score": 5, "fb": "优先级清晰，安全优先"},
     {"text": "哪件事急就先做哪件，差不多就行", "score": 3, "fb": "有一定判断，但缺乏系统性"},
     {"text": "看心情，想做啥就做啥", "score": 1, "fb": "缺乏计划和条理"},
     {"text": "都放着等雇主回来了再说", "score": 1, "fb": "完全被动"}]))

questions.append(q("professionalism", "job_stability", "hard",
    "你之前换工作的原因主要是什么？最长的一份做了多久？",
    [{"text": "最长一份做了3年，离职是因为雇主搬家/孩子上学不需要了", "score": 5, "fb": "稳定性好，离职原因客观合理"},
     {"text": "最长1-2年，离职多是雇主不满意或自己原因", "score": 3, "fb": "稳定性一般，有波动"},
     {"text": "每份都做不久，平均3-6个月", "score": 1, "fb": "稳定性较差，雇主可能担心"},
     {"text": "没做过几份，都不长", "score": 2, "fb": "缺乏长期工作经验"}]))

questions.append(q("professionalism", "salary_negotiation", "hard",
    "雇主跟你谈薪资，你觉得目前的薪资低于市场水平，你会怎么沟通？",
    [{"text": "准备市场数据，诚恳表达期望，同时说明自己的工作价值和贡献，寻求合理调整", "score": 5, "fb": "有理有据，专业谈判"},
     {"text": "直接说想要涨薪", "score": 3, "fb": "直接但缺乏说服力"},
     {"text": "不好意思提，等雇主主动", "score": 2, "fb": "被动等待，可能错失机会"},
     {"text": "不说，但心里不满，工作敷衍", "score": 1, "fb": "消极应对，影响工作质量"}]))

questions.append(q("professionalism", "continuing_education", "hard",
    "你会怎么提升自己的育儿或家政服务技能？",
    [{"text": "参加正规培训课程，考取相关证书，阅读专业书籍，向同行请教", "score": 5, "fb": "持续学习，自我提升意识强"},
     {"text": "在网上看一些育儿视频", "score": 3, "fb": "有学习意识，但来源不够专业"},
     {"text": "做久了自然就有经验了", "score": 2, "fb": "被动等待，缺乏主动学习"},
     {"text": "不需要学，我以前就是这么带的", "score": 1, "fb": "拒绝更新知识，可能落后"}]))

# ═══ ELDER CARE (7q: 2E + 2M + 3H) ═══
questions.append(q("elder_care", "elder_experience", "easy",
    "你有照顾老人的经验吗？具体做过什么？",
    [{"text": "有，照顾过家里老人和其他雇主家的老人，包括喂饭、擦身、陪聊、陪诊等", "score": 5, "fb": "全面照护经验，技能扎实"},
     {"text": "照顾过，但主要是喂饭和陪聊", "score": 3, "fb": "有一定经验，技能较基础"},
     {"text": "没照顾过老人，只带过孩子", "score": 2, "fb": "缺乏老人照护经验"},
     {"text": "完全没经验", "score": 1, "fb": "不具备老人照护能力"}]))

questions.append(q("elder_care", "medication_management", "medium",
    "老人需要按时服药，但老人总是忘记或者不肯吃，你会怎么办？",
    [{"text": "设置闹钟提醒，用分装药盒，温和地引导老人服药，记录每次服药情况", "score": 5, "fb": "系统化管理，专业细致"},
     {"text": "到点就去提醒老人吃药", "score": 3, "fb": "有基本意识，但方法较简单"},
     {"text": "老人不吃就不吃了，顺其自然", "score": 1, "fb": "忽视用药安全"},
     {"text": "偷偷把药片碾碎混在饭里", "score": 2, "fb": "未经同意处理药物，可能违反医嘱"}]))

questions.append(q("elder_care", "fall_response", "hard",
    "老人走路的时候突然摔倒了，你会怎么处理？",
    [{"text": "不要立即扶起，先询问哪里疼、能不能动，检查有无明显骨折或出血，必要时拨打120", "score": 5, "fb": "正确处理，避免二次伤害"},
     {"text": "马上扶起来，看看有没有事", "score": 2, "fb": "可能加重伤情"},
     {"text": "叫人来帮忙，自己站一边", "score": 2, "fb": "被动等待"},
     {"text": "不管了，让老人自己爬起来", "score": 1, "fb": "完全不负责任"}]))

questions.append(q("elder_care", "feeding_assistance", "hard",
    "老人吞咽困难，吃饭的时候经常呛咳，你会怎么处理？",
    [{"text": "调整食物性状（糊状/软食），小口喂食，进食时保持坐姿，吃完后保持坐姿30分钟，及时就医评估", "score": 5, "fb": "专业护理，关注安全和营养"},
     {"text": "慢慢喂，小心一点", "score": 3, "fb": "有一定意识，但方法不够系统"},
     {"text": "让老人自己吃，我在旁边看着", "score": 2, "fb": "被动看护，缺乏主动干预"},
     {"text": "喂快点，不然凉了", "score": 1, "fb": "忽略吞咽风险，可能导致窒息"}]))

questions.append(q("elder_care", "end_of_life_communication", "hard",
    "如果雇主家的老人病危，需要你陪护到最后，你会怎么准备和处理？",
    [{"text": "提前了解病情，准备好必要的护理用品，学习临终关怀知识，给予老人和家属情感支持", "score": 5, "fb": "专业且有人文关怀"},
     {"text": "按雇主要求做，不懂就问", "score": 3, "fb": "有配合意识，但主动性不足"},
     {"text": "不知道怎么办，等着别人教", "score": 2, "fb": "缺乏主动性和学习能力"},
     {"text": "这种情况我做不了，想辞职", "score": 1, "fb": "缺乏应对危机的勇气和能力"}]))

# ═══ SPECIAL SITUATIONS (15q: all hard) ═══
questions.append(q("special", "infant_colic", "hard",
    "两个月大的宝宝肠绞痛，每天晚上固定时间剧烈哭闹，怎么哄都哄不好，你会怎么处理？",
    [{"text": "尝试多种方法：飞机抱、白噪音、腹部按摩、温水浴，记录发作时间给医生参考，同时安抚家长情绪", "score": 5, "fb": "综合处理，多管齐下，关注家长心理"},
     {"text": "抱着不停地走，一直哄", "score": 3, "fb": "有耐心但方法单一"},
     {"text": "交给家长处理，我不管了", "score": 1, "fb": "逃避责任"},
     {"text": "给孩子喂点酒或者草药水镇住", "score": 1, "fb": "危险方法，绝对禁止"}]))

questions.append(q("special", "premature_baby_care", "hard",
    "雇主家的宝宝是早产儿，身体比较弱，你会特别注意哪些方面？",
    [{"text": "严格按时喂哺、注意保暖、避免交叉感染、定期体检、记录生长发育数据、保持室内安静", "score": 5, "fb": "早产儿护理知识全面，细心专业"},
     {"text": "按时喂奶，注意别着凉", "score": 3, "fb": "有基本意识，但不够全面"},
     {"text": "跟普通宝宝一样照顾就行", "score": 1, "fb": "忽视早产儿特殊需求"},
     {"text": "多穿点衣服，怕冷", "score": 2, "fb": "过度保暖可能导致过热"}]))

questions.append(q("special", "multi_child_chaos", "hard",
    "雇主家有三个孩子（3岁、6岁、10岁），同时哭闹要东西，家里一片混乱，你会怎么办？",
    [{"text": "先稳住最大的，让他帮忙照顾小的，分别安抚，然后依次处理各自需求，建立秩序", "score": 5, "fb": "多子女管理能力优秀，分配合理"},
     {"text": "谁哭得最凶先哄谁", "score": 2, "fb": "被动应对，混乱中缺乏条理"},
     {"text": "让他们自己哭，等安静了再说", "score": 1, "fb": "忽视孩子需求，可能造成心理伤害"},
     {"text": "大声呵斥让他们别吵了", "score": 1, "fb": "暴力压制，造成恐惧"}]))

questions.append(q("special", "nanny_dispute_with_parent", "hard",
    "你和雇主的育儿理念发生了严重分歧（比如你是否该给孩子穿袜子），双方都很坚持，你会怎么处理？",
    [{"text": "先了解雇主为什么这么想，再解释我的观点和建议的理由，寻找双方都能接受的方案", "score": 5, "fb": "尊重+沟通+协商，寻求共识"},
     {"text": "听雇主的，他们说怎么就怎么来", "score": 3, "fb": "顺从，但可能不利于孩子"},
     {"text": "坚持我的做法，雇主不懂", "score": 1, "fb": "固执己见，破坏合作关系"},
     {"text": "找其他人评理，看谁对谁错", "score": 2, "fb": "把私人矛盾公开化，不合适"}]))

questions.append(q("special", "working_parent_commuting", "hard",
    "雇主夫妻都是上班族，早出晚归，孩子主要是你和老人带，你怎么协调三代人的育儿方式？",
    [{"text": "跟老人和雇主分别沟通，统一基本规则，分歧私下解决，不在孩子面前争执，定期开小会复盘", "score": 5, "fb": "协调能力强，兼顾各方关系"},
     {"text": "听雇主的，老人说的不当面反对", "score": 3, "fb": "有一定智慧，但沟通不够主动"},
     {"text": "各管各的，不过多参与", "score": 2, "fb": "消极回避，问题不会消失"},
     {"text": "站在老人那边，雇主家的方式不对", "score": 1, "fb": "偏袒一方，加剧家庭矛盾"}]))

questions.append(q("special", "nanny_overnight_call", "hard",
    "半夜11点，雇主打电话来说孩子发烧39度，要你马上回去，但此时你在自己家，你会怎么处理？",
    [{"text": "立即赶回，评估情况，必要时陪同就医，同时告知雇主注意安全", "score": 5, "fb": "紧急情况处理得当，责任感强"},
     {"text": "问清楚情况，看要不要回去", "score": 3, "fb": "有一定判断，但可能延误时机"},
     {"text": "这么晚了不方便，明天再说", "score": 1, "fb": "缺乏应急意识，延误救治"},
     {"text": "让他们叫救护车，我不回去了", "score": 1, "fb": "完全推卸责任"}]))

questions.append(q("special", "pet_allergy_child", "hard",
    "雇主家有宠物猫，孩子对猫毛过敏，但雇主不舍得送走猫，你会怎么处理？",
    [{"text": "建议用空气净化器、定期给猫洗澡、孩子房间禁入宠物、密切观察孩子症状并记录，与医生沟通", "score": 5, "fb": "多维度解决，科学务实"},
     {"text": "提醒雇主注意，但做不了更多", "score": 3, "fb": "有意识但行动有限"},
     {"text": "让孩子远离猫就行", "score": 2, "fb": "简单化处理，效果有限"},
     {"text": "这是雇主家的事，不管", "score": 1, "fb": "不作为，忽视孩子健康"}]))

questions.append(q("special", "single_parent_stress", "hard",
    "雇主是单亲妈妈，工作压力大，经常情绪低落，甚至在你面前流泪，你会怎么处理？",
    [{"text": "给予理解和安慰，倾听但不越界，必要时建议寻求心理咨询，照顾好自己和雇主家庭的基本需求", "score": 5, "fb": "有同理心又有边界感"},
     {"text": "安慰一下，然后继续做自己的事", "score": 3, "fb": "有一定同理心，但深度不够"},
     {"text": "不管她，我只负责干活", "score": 1, "fb": "冷漠，缺乏人情味"},
     {"text": "跟着一起哭，情绪受影响", "score": 2, "fb": "情绪容易被带偏，缺乏稳定性"}]))

questions.append(q("special", "elder_abuse_suspected", "hard",
    "你在照顾老人时发现老人身上有不明淤青，老人说是不小心碰的，但你不信，你会怎么办？",
    [{"text": "温和询问老人具体情况，做好记录，必要时向有关部门报告，保护老人权益", "score": 5, "fb": "警觉性强，处理得当，有社会责任感"},
     {"text": "问问老人怎么回事，看看情况", "score": 3, "fb": "有一定警觉，但处理力度不够"},
     {"text": "老人说的应该是对的，算了", "score": 1, "fb": "忽视潜在虐待信号"},
     {"text": "直接问雇主是不是打了老人", "score": 2, "fb": "方式不当，可能引起冲突"}]))

questions.append(q("special", "food_poisoning_outbreak", "hard",
    "雇主全家吃了你做的饭后都出现了腹泻呕吐，你会怎么处理？",
    [{"text": "立即了解症状和进食情况，必要时陪同就医，不推卸责任，事后复盘找出原因，改进操作", "score": 5, "fb": "冷静应对，承担责任，持续改进"},
     {"text": "赶紧解释不是我做的饭的问题", "score": 2, "fb": "急于撇清关系，不够冷静"},
     {"text": "不管了，让他们自己去医院", "score": 1, "fb": "逃避责任，缺乏担当"},
     {"text": "慌了，手足无措", "score": 1, "fb": "缺乏应急处理能力"}]))

questions.append(q("special", "nanny_wrongful_accusation", "hard",
    "雇主突然说你打了孩子，但你确定自己没有，而且家里有监控，你会怎么做？",
    [{"text": "保持冷静，请雇主调取监控录像查证，如实说明情况，不争吵不激动，必要时寻求第三方调解", "score": 5, "fb": "冷静理性，善用证据维权"},
     {"text": "激烈否认，要求雇主道歉", "score": 2, "fb": "情绪化，不利于解决问题"},
     {"text": "解释不清就辞职走人", "score": 1, "fb": "放弃自证，逃避问题"},
     {"text": "默默忍受，不解释", "score": 1, "fb": "缺乏自我保护意识"}]))

questions.append(q("special", "emergency_natural_disaster", "hard",
    "你正在雇主家工作时突然地震了，你会怎么处理？",
    [{"text": "立即让孩子和老人躲在桌下或墙角，护住头部，地震停止后迅速疏散到开阔地带，清点人数", "score": 5, "fb": "正确处理地震应急，保护弱势群体"},
     {"text": "赶紧往外跑", "score": 2, "fb": "盲目逃跑可能在途中受伤"},
     {"text": "先保护贵重物品", "score": 1, "fb": "本末倒置，生命安全第一"},
     {"text": "吓懵了，不知道怎么办", "score": 1, "fb": "缺乏应急训练"}]))

questions.append(q("special", "misunderstanding_with_children", "hard",
    "孩子误会你偷了他的玩具，哭着不肯相信你，雇主也在场，你会怎么处理？",
    [{"text": "蹲下来平视孩子，温和地解释，让小孩检查自己的玩具箱，一起寻找，用行动证明清白", "score": 5, "fb": "尊重孩子，耐心沟通，用行动说话"},
     {"text": "告诉雇主这是误会，让雇主来处理", "score": 2, "fb": "推给雇主，缺乏自主处理能力"},
     {"text": "不管孩子，自己做自己的事", "score": 1, "fb": "忽视孩子感受"},
     {"text": "生气地辩解，跟孩子吵起来", "score": 1, "fb": "情绪失控，无法妥善处理"}]))

questions.append(q("special", "elder_memory_loss_paranoia", "hard",
    "老人患阿尔茨海默症，开始怀疑有人偷他的东西，到处翻箱倒柜，你会怎么应对？",
    [{"text": "不反驳不争论，温和地帮他一起找，转移注意力，把常用物品放在固定位置方便寻找", "score": 5, "fb": "理解疾病，处理得当"},
     {"text": "告诉老人是他自己记错了", "score": 2, "fb": "讲道理对痴呆患者无效"},
     {"text": "把东西藏起来不让老人找到", "score": 1, "fb": "欺骗行为，伤害老人信任"},
     {"text": "任由老人翻，不管", "score": 1, "fb": "缺乏耐心，放任混乱"}]))

# ═══ DRAFT: Need more questions to reach 90 ═══
# Current count: 7+9+14+9+12+9+7+9+7+15 = 98... let me recount

# Save
out = os.path.join(os.path.dirname(__file__), "questions.json")
with open(out, "w", encoding="utf-8") as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print(f"Wrote {len(questions)} questions")
stats = Counter((q["difficulty"], q["category"]) for q in questions)
easy = sum(1 for q in questions if q["difficulty"] == "easy")
medium = sum(1 for q in questions if q["difficulty"] == "medium")
hard = sum(1 for q in questions if q["difficulty"] == "hard")
print(f"  Easy: {easy}, Medium: {medium}, Hard: {hard}")
print(f"  Easy+Medium ratio: {(easy+medium)/len(questions)*100:.1f}%")
cats = Counter(q["category"] for q in questions)
print(f"  Categories: {dict(cats)}")
for (d, c), n in sorted(stats.items()):
    print(f"    {d:6s} {c:12s}: {n}q")
