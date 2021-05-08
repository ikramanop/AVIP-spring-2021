import os

if __name__ == '__main__':
    with open('./work_5/README.md', 'a+') as file:
        for i in sorted(os.listdir("pictures_results/work_5/symbols"), key=lambda x: int(x.split('.')[0])):
            file.write(f"![imgOut](../pictures_results/work_5/symbols/{i}) ")
