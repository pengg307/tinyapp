"""Add translated figure bio fields for all 7 languages"""
import json
from pathlib import Path

BASE = Path(r"E:\aiprojects\tinyapp\career_course")
figures_file = BASE / "src/data/figures.json"

with open(figures_file, "r", encoding="utf-8") as f:
    data = json.load(f)

# Translation templates for each figure
# Format: {figure_id: {lang: {field: translated_text}}}
FIGURE_TRANS = {
    "isaac_newton": {
        "zh": {"early_career": "剑桥大学三一学院学生，受疫情隔离影响深度专注数学与自然哲学。", "early_actions": "在隔离期间发展了微积分、光学和万有引力理论。", "breakthrough": "1687年出版《自然哲学的数学原理》，奠定经典力学基础。", "key_lesson": "如果我看得更远，那是因为我站在巨人的肩膀上。"},
        "en": {"early_career": "Student at Trinity College, Cambridge, deeply focused on mathematics and natural philosophy during the plague lockdown.", "early_actions": "Developed calculus, optics, and the theory of universal gravitation during isolation.", "breakthrough": "Published Principia Mathematica in 1687, laying the foundation for classical mechanics.", "key_lesson": "If I have seen further, it is by standing on the shoulders of giants."},
        "es": {"early_career": "Estudiante en Trinity College, Cambridge, enfocado en matemáticas y filosofía natural durante el aislamiento de la peste.", "early_actions": "Desarrolló el cálculo, óptica y la teoría de la gravitación universal durante el aislamiento.", "breakthrough": "Publicó Principia Mathematica en 1687, sentando las bases de la mecánica clásica.", "key_lesson": "Si he visto más lejos, es por estar de pie sobre los hombros de gigantes."},
        "ja": {"early_career": "トリニティ・カレッジの学生。ペストの隔離中に数学と自然哲学に深く集中した。", "early_actions": "隔離中に微積分、光学、万有引力理論を発展させた。", "breakthrough": "1687年に『自然哲学の数学原理』を出版し、古典力学の基礎を築いた。", "key_lesson": "もし私が farther に見られるならば、それは巨人の肩に乗っているからです。"},
        "de": {"early_career": "Student am Trinity College Cambridge, konzentrierte sich während der Pestisolierung auf Mathematik und Naturphilosophie.", "early_actions": "Entwickelte during Isolation infinitesimalrechnung, Optik und die Theorie der universellen Gravitation.", "breakthrough": "Veröffentlichte Principia Mathematica 1687 und legte die Grundlage für die klassische Mechanik.", "key_lesson": "Wenn ich weiter gesehen habe, dann weil ich auf den Schultern von Riesen stehe."},
        "ru": {"early_career": "Студент Тринити-колледжа Кембриджа, глубоко сосредоточенный на математике и натуральной философии во время карантина.", "early_actions": "Разработал математический анализ, оптику и теорию всемирного тяготения во время изоляции.", "breakthrough": "Опубликовал Principia Mathematica в 1687 году, заложив основы классической механики.", "key_lesson": "Если я видел дальше других, то стоя на плечах гигантов."},
        "fr": {"early_career": "Étudiant au Trinity College de Cambridge, profondément concentré sur les mathématiques et la philosophie naturelle pendant le confinement de la peste.", "early_actions": "A développé le calcul infinitésimal, l'optique et la théorie de la gravitation universelle pendant l'isolement.", "breakthrough": "A publié Principia Mathematica en 1687, jetant les bases de la mécanique classique.", "key_lesson": "Si j'ai vu plus loin, c'est en me tenant sur les épaules des géants."},
    },
    "albert_einstein": {
        "zh": {"early_career": "瑞士专利局职员，业余研究物理学。", "early_actions": "1905年发表四篇开创性论文，包括狭义相对论和质能方程。", "breakthrough": "1921年获诺贝尔物理学奖，创立广义相对论。", "key_lesson": "想象力比知识更重要。"},
        "en": {"early_career": "Swiss patent office clerk, studied physics as a hobby.", "early_actions": "Published four groundbreaking papers in 1905, including special relativity and E=mc².", "breakthrough": "Won Nobel Prize in Physics 1921, developed general relativity.", "key_lesson": "Imagination is more important than knowledge."},
        "es": {"early_career": "Funcionario de la oficina de patentes suiza, estudió física como pasatiempo.", "early_actions": "Publicó cuatro artículos revolucionarios en 1905, incluyendo la relatividad especial y E=mc².", "breakthrough": "Ganó el Premio Nobel de Física en 1921, desarrolló la relatividad general.", "key_lesson": "La imaginación es más importante que el conocimiento."},
        "ja": {"early_career": "スイス特許局職員。物理学を趣味で研究した。", "early_actions": "1905年に特殊相対性理論やE=mc²など4つの画期的論文を発表。", "breakthrough": "1921年にノーベル物理学賞受賞、一般相対性理論を確立。", "key_lesson": "想像力は知識よりも重要である。"},
        "de": {"early_career": "Schweizer Patentamtangestellter, studierte Physik als Hobby.", "early_actions": "Veröffentlichte vier bahnbrechende Papers 1905, einschließlich spezieller Relativität und E=mc².", "breakthrough": "Gewann den Nobelpreis für Physik 1921, entwickelte die allgemeine Relativitätstheorie.", "key_lesson": "Phantasie ist wichtiger als Wissen."},
        "ru": {"early_career": "Сотрудник швейцарского патентного ведомства, изучал физику как hobby.", "early_actions": "Опубликовал четыре новаторских работы в 1905 году, включая специальную теорию относительности и E=mc².", "breakthrough": "Получил Нобелевскую премию по физике в 1921 году, развил общую теорию относительности.", "key_lesson": "Воображение важнее знания."},
        "fr": {"early_career": "Fonctionnaire au bureau des brevets suisse, étudiait la physique comme hobby.", "early_actions": "Publia quatre articles révolutionnaires en 1905, y compris la relativité restreinte et E=mc².", "breakthrough": "Gagna le Prix Nobel de Physique en 1921, développa la relativité générale.", "key_lesson": "L'imagination est plus importante que le savoir."},
    },
    "marie_curie": {
        "zh": {"early_career": "华沙女性，后赴巴黎索邦大学求学。", "early_actions": "发现钋和镭元素，开创放射性研究。", "breakthrough": "首位两获诺贝尔奖的人（物理1903、化学1911）。", "key_lesson": "生活中没有什么可怕的东西，只有需要理解的东西。"},
        "en": {"early_career": "Woman from Warsaw, later studied at Sorbonne in Paris.", "early_actions": "Discovered polonium and radium, pioneered radioactivity research.", "breakthrough": "First person to win two Nobel Prizes (Physics 1903, Chemistry 1911).", "key_lesson": "Nothing in life is to be feared, it is only to be understood."},
        "es": {"early_career": "Mujer de Varsovia, luego estudió en la Sorbona de París.", "early_actions": "Descubrió el polonio y el radio, pionera en investigación de radiactividad.", "breakthrough": "Primera persona en ganar dos Premios Nobel (Física 1903, Química 1911).", "key_lesson": "Nada en la vida debe ser temido, solo comprendido."},
        "ja": {"early_career": "ワルシャワ出身の女性。後にパリ・ソルボンヌ大学で学んだ。", "early_actions": "ポロニウムとラジウムを発見し、放射性研究を先導した。", "breakthrough": "2度のノーベル賞受賞者（物理学1903、化学1911）。", "key_lesson": "人生に恐れられるべきものは何もなく、理解されるべきものだけである。"},
        "de": {"early_career": "Frau aus Warschau, studierte später an der Sorbonne in Paris.", "early_actions": "Entdeckte Polonium und Radium, Pionierin der Radioaktivitätsforschung.", "breakthrough": "Erste Person mit zwei Nobelpreisen (Physik 1903, Chemie 1911).", "key_lesson": "Nichts im Leben ist zu fürchten, es ist nur zu verstehen."},
        "ru": {"early_career": "Женщина из Варшавы, позже училась в Сорбонне в Париже.", "early_actions": "Открыла полоний и радий, пионер в исследовании радиоактивности.", "breakthrough": "Первый человек, получивший две Нобелевские премии (физика 1903, химия 1911).", "key_lesson": "В жизни нет ничего страшного, есть только то, что нужно понять."},
        "fr": {"early_career": "Femme de Varsovie, étudia plus tard à la Sorbonne à Paris.", "early_actions": "Découvrit le polonium et le radium, pionnière de la recherche sur la radioactivité.", "breakthrough": "Première personne à gagner deux Prix Nobel (Physique 1903, Chimie 1911).", "key_lesson": "Rien en cette vie ne doit être craint, il n'y a que Compréhension."},
    },
}

# Add translations to figures
for fig in data["figures"]:
    fig_id = fig.get("id", "")
    if fig_id in FIGURE_TRANS:
        trans = FIGURE_TRANS[fig_id]
        for lang, texts in trans.items():
            for field in ["early_career", "early_actions", "breakthrough", "key_lesson"]:
                key = f"{field}_{lang}"
                if key not in fig:
                    fig[key] = texts.get(field, fig.get(field, ""))

# Save
with open(figures_file, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✓ Added translations for {len(FIGURE_TRANS)} figures")
