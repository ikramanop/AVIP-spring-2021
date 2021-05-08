IMAGES = {
    "Портрет": "nando",
    "Фотография рукописного текста": "integral",
    "Фотография печатного текста": "text"
}

if __name__ == '__main__':
    with open("./work_2/README.md", "a") as file:
        for title, dirr in IMAGES.items():
            file.write(f"\n### {title}\n")
            for i in range(1, 10):
                file.write(f"""
#### {i}/9

![{dirr}](../pictures_results/work_2/{dirr}/{i}_of_9.png)
""")
