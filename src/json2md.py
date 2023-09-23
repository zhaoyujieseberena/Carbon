# %%
import json
import os
from csv2json import run

run()

def load_head(file):
    with open("./res/head.md", 'r') as f:
        for line in f:
            file.write(line)
        file.write("\n")


'''

    path = 'res/papers.json'
    

    for pf in sorted(os.listdir(path)):
        if not pf.endswith(".json"):
            continue
        with open(os.path.join(path, pf), 'r') as f:
            title = json.load(f)['title']
            file.write("  - [{}](#{})\n".format(title, title.lower().replace(' ', '-')))

    file.write("- [Contribute](#contribute)\n")
'''


def load_report(file):
    file.write("## The parameters sources\n")
    

    path = './res/datasets.json'
    
    with open(path, 'r') as f:
            table = json.load(f)
            file.write("#### A summary of parameters sources\n")
            file.write('A list of some links that can be used as sources formodeling and calculating parameters\n')

            
            file.write("| Title | Link | Descriptions |  \n")
            file.write("| :--- | :----  | :-------- | \n")
            j=0

            for metric in table:
                j+=1
                
                file.write("|{}".format(metric['Description']))
                
                file.write(" |[[{}]]({})".format(metric['status'],metric['Link']))
                #choose(file,metric['Computer system stack '])
                #choose(file,metric['Hardware system'])
                
                #choose(file,metric['Included carbon life cycle stage'])
                file.write("|{}".format(metric['Descriptions']))
                file.write("|\n")
            file.write("\n")
            file.write("#### Application scope of parameters sources\n")

            file.write("| Title |  Carbon life cycle stage | Computer system stack | Hardware system | \n")
            file.write("| :--- | :---- | :------| :------ |  \n")
            j=0


            for metric in table:
                j+=1
                
                file.write("|{}".format(metric['Description']))
                
                
                choose(file,metric['Computer system stack '])
                choose(file,metric['Hardware system'])
                
                choose(file,metric['Included carbon life cycle stage'])
               
                file.write("|\n")
            file.write("\n")

    

        

            '''
                file.write("- [**{}**]".format(paper['venue']))
                file.write(" {}".format(paper['name']))
                file.write(" (*{}*)".format(paper['affiliation']))
                if 'link' in paper:
                    file.write(" [[paper]]({})".format(paper['link']))
                    cite = citation[paper['name']]['citation']
                    file.write("![Scholar citations](https://img.shields.io/badge/Citations-{}-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)".format(cite))
                if 'source' in paper:
                    source = paper['source']
                    file.write(" [[code]]({})".format(source))
                    repo = source.split('github.com/', 1)[1]
                    if repo.count('/') == 1:
                        file.write("![GitHub stars](https://img.shields.io/github/stars/{}.svg?logo=github&label=Stars)".format(repo))

                file.write("\n")
                '''
def define(file,string):
    if '1' in string: file.write("|![1](image/yes.svg)" )
    if '0' in string: file.write("|![1](image/no.svg)" )


def load_Link(file):
    file.write("## Tools\n")
    

    path = './res/tools.json'
    
    
    with open(path, 'r') as f:
            table = json.load(f)
            

            file.write("| ID | Name | Link   | Description | \n")
            file.write("| :-: | :-: |  :----: | :--------- |\n")
            
            j=0
            for paper in table:
                    j+=1
                    file.write("|{}<a name='Link{}'></a>".format(j,j))
                    file.write("|{}".format(paper['Name']))
                    file.write(" |[[code]]({})".format(paper['Link']))
                   
                    
                    if (paper['Paper Link']): file.write(" [[paper]]({})".format(paper['Paper Link']))
                    file.write("|{}".format(paper['Description']))
                    file.write("|")
                    file.write("\n")

            file.write("\n")

            
            file.write("| ID | Name  | Target problem | Computer system stack | Hardware system | Carbon life cycle stage | \n")
            file.write("| :---: | :--- | :---- | :------ | :----- | :-------- | \n")
            j=0

            for metric in table:
                j+=1
                file.write("|[{}](#Link{})".format(j,j))
                file.write("|{}".format(metric['Name']))
                choose(file,metric['Target Problem'])
                
                choose(file,metric['Computer system stack '])
                choose(file,metric['Hardware system'])
                
                choose(file,metric['Included carbon life cycle stage'])
                file.write("|\n")
            file.write("\n")


            file.write("#### a summary of metrics can be calculated by tools \n")
            file.write("|ID| Tools| PUE | CUE | GPUE | CCI | SCI | ASC | JSC | CDP/<br>CEP | tCDP/<br>tCEP| \n")
            file.write("|:-:| :- | :-: |  :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |\n")
            
            j=0
            for paper in table:
                    j+=1
                    file.write("|[{}](#Link{})".format(j,j))
                    file.write("|{}".format(paper['Name']))
                    
                    define(file,paper['Name'])
                    define(file,paper['PUE'])
                    define(file,paper['CUE'])
                    define(file,paper['GPUE'])
                    define(file,paper['CCI'])
                    define(file,paper['SCI'])
                    define(file,paper['ASC'])
                    define(file,paper['JSC'])
                    define(file,paper['CDP/CEP'])
                    define(file,paper['tCDP/tCEP'])
                  
                    
                    
                    file.write("|")
                    file.write("\n")

            file.write("\n")

            file.write("### Operational carbon modeling method\n")
            file.write("| Tools| Operational energy | Operational usage | Operational carbon intensity |  \n")
            file.write("| :-: | :- |  :- | :- | \n")
            
            j=0
            for paper in table:
                    j+=1
                    file.write("|{}".format(paper['Name']))
                    
                    file.write("| CPU:{}<br> GPU:{}".format(paper['Operation CPU energy'],paper['Operation GPU energy']))
                    file.write("|CPU:{}<br> GPU:{}".format(paper['Operation CPU usage'],paper['Operation GPU usage']))
                    file.write("| {}".format(paper['Operation intensity']))
                    
                  
                    
                    
                    file.write("|")
                    file.write("\n")

            file.write("\n")

            file.write("### Embodied carbon modeling method\n")
            file.write("| Tools | Embodied energy | Embodied carbon intensity | \n")
            file.write("| :-: | :- | :- |\n")
            
            j=0
            for paper in table:
                    j+=1
                    if 'Manufacturing' in paper['Included carbon life cycle stage']:
                        file.write("|{}".format(paper['Name']))
                        
                        
                        file.write("| {}".format(paper['Embodied carbon']))
                        file.write("| {}".format(paper['Embodied carbon intensity']))

                    
                        
                        
                        file.write("|")
                        file.write("\n")

            file.write("\n")
            '''
                file.write("- [**{}**]".format(paper['venue']))
                file.write(" {}".format(paper['name']))
                file.write(" (*{}*)".format(paper['affiliation']))
                if 'link' in paper:
                    file.write(" [[paper]]({})".format(paper['link']))
                    cite = citation[paper['name']]['citation']
                    file.write("![Scholar citations](https://img.shields.io/badge/Citations-{}-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)".format(cite))
                if 'source' in paper:
                    source = paper['source']
                    file.write(" [[code]]({})".format(source))
                    repo = source.split('github.com/', 1)[1]
                    if repo.count('/') == 1:
                        file.write("![GitHub stars](https://img.shields.io/github/stars/{}.svg?logo=github&label=Stars)".format(repo))

                file.write("\n")
                '''




def load_paper(file):
    file.write("## Papers\n")

    with open('./.github/citation/citation.json', 'r') as f:
        citation = json.load(f)

    path = './res/papers.json'
    
    with open(path, 'r') as f:
            table = json.load(f)
            file.write("### Papers overview\n")
            file.write("We have listed some relevant literature in the field of sustainable computer systems below.\n")

            file.write("| ID | Venue  | Title | Affiliation | &nbsp;&nbsp;&nbsp;&nbsp;Link&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | \n")
            file.write("| :-: | :-: | :----: | :---------: | :---: |\n")
            
            j=0
            for paper in table:
                    j+=1
                    file.write("{}<a name='paper{}'></a>".format(j,j))
                    file.write("|{} <br>{}|".format(paper['Venue'],(paper['Year'])))
                    file.write("{}|".format(paper['Title']))
                    file.write("{}|".format(paper['School/Insititution']))
                    file.write(" [[paper]]({})".format(paper['Link']))
                    cite = citation[paper['Title']]['citation']
                    file.write("![Scholar citations](https://img.shields.io/badge/Citations-{}-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)".format(cite))
                    file.write("|")
                    file.write("\n")

            file.write("\n")
            file.write("### Papers' application scope\n")

            
            file.write("| Link | Target problem | Carbon life cycle stage | Hardware system | Computer system stack | Datacenter stack |   \n")
            file.write("| :---: | :---- | :------ | :------ | :-------- |:-------- | \n")
            j=0

            

            for metric in table:
                j+=1
                file.write("|[{}](#paper{})".format(j,j))
                choose(file,metric['Target Problem'])
                choose(file,metric['Included carbon life cycle stage'])
                choose(file,metric['Hardware system'])
                choose(file,metric['Computer system stack '])
                choose(file,metric['Datacenter stack'])
                
                
                
                file.write("|\n")
            file.write("\n")

            
        

            '''
                file.write("- [**{}**]".format(paper['venue']))
                file.write(" {}".format(paper['name']))
                file.write(" (*{}*)".format(paper['affiliation']))
                if 'link' in paper:
                    file.write(" [[paper]]({})".format(paper['link']))
                    cite = citation[paper['name']]['citation']
                    file.write("![Scholar citations](https://img.shields.io/badge/Citations-{}-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)".format(cite))
                if 'source' in paper:
                    source = paper['source']
                    file.write(" [[code]]({})".format(source))
                    repo = source.split('github.com/', 1)[1]
                    if repo.count('/') == 1:
                        file.write("![GitHub stars](https://img.shields.io/github/stars/{}.svg?logo=github&label=Stars)".format(repo))

                file.write("\n")
                '''

def load_legend(file):
    
    with open("./res/legend.md", 'r') as f:
        for line in f:
            file.write(line)
    

def choose(file,string):
    i=0
    file.write("|")
    if 'N/A' in string:
        i+=1
        if i>1:
             i=1
             file.write("<br>")
        file.write("N/A")
    if 'Platform' in string:
        i+=1
        if i>1:
             i=1
             file.write("<br>")
        file.write("[![1](image/Platform.svg) Platform ](Classification/Datacenter_stack.md#Platform)")
    if 'Optimization' in string:
        i+=1
        if i>1:
             i=1
             file.write("<br>")
        file.write("[![1](image/Optimization.svg) Opt ](Classification/Target_Problem.md#Optimization)")
    if 'Application' in string:
        i+=1
        if i>1:
             i=1
             file.write("<br>")
        file.write("[![1](image/App.svg) App ](Classification/Computer_system_stack.md#Application)")
    if 'Datacenter' in string:
        i+=1
        if i>1:
             i=1
             file.write("<br>")
        file.write("[![1](image/center.svg) DC ](Classification/Hardware_system.md#Datacenter)")
    if 'Manufacturing' in string:
        i+=1
        if i>1:
             i=1
             file.write("<br>")
        file.write("[![1](image/Manufacturing.svg) MF ](Classification/Included_carbon_life_cycle_stage.md#Manufacturing)")
    if 'Modeling' in string:
        i+=1
        if i>1:
             i=1
             file.write("<br>")
        file.write("[![1](image/Modeling.svg) Mod. ](Classification/Target_Problem.md#Modeling)")
    if 'OS' in string:
        i+=1
        if i>1:
             i=1
             file.write("<br>")
        file.write("[![1](image/OS.svg) OS ](Classification/Computer_system_stack.md#OS)")
    if 'Edge' in string:
        i+=1
        if i>1:
             i=1
             file.write("<br>")
        file.write("[![1](image/Edge.svg) Edge ](Classification/Hardware_system.md#Edge.md)")
    if 'Operation' in string:
        i+=1
        if i>1:
             i=1
             file.write("<br>")
        file.write("[![1](image/Operation.svg) Op ](Classification/Included_carbon_life_cycle_stage.md#Operation)")
    if 'Standardization' in string:
        i+=1
        if i>1:
             i=1
             file.write("<br>")
        file.write("[![1](image/Stand.svg) Stand. ](Classification/Target_Problem.md#Standardization)")
    if 'Microarchitecture' in string:
        i+=1
        if i>1:
             i=1
             file.write("<br>")
        file.write("[![1](image/Micro.svg) Micro. ](Classification/Computer_system_stack.md#Microarchitecture)")
    if 'Mobile' in string:
        i+=1
        if i>1:
             i=1
             file.write("<br>")
        file.write("[![1](image/Mobile.svg) Mobile ](Classification/Hardware_system.md#Mobile)")
    if 'End-of-life' in string:
        i+=1
        if i>1:
             i=1
             file.write("<br>")
        file.write("[![1](image/End-of-life.svg) E-o-l ](Classification/Included_carbon_life_cycle_stage.md#End-of-life)")
    if 'Review' in string:
        i+=1
        if i>1:
             i=1
             file.write("<br>")
        file.write("[![1](image/Review.svg) Review ](Classification/Target_Problem.md#Review)")
    if 'Infrastructure' in string:
        i+=1
        if i>1:
             i=1
             file.write("<br>")
        file.write("[![1](image/Infrastructure.svg) Infra ](Classification/Computer_system_stack.md#Infrastructure)")
    if 'Tiny' in string:
        i+=1
        if i>1:
             i=1
             file.write("<br>")
        file.write("[![1](image/Tiny.svg) Tiny ](Classification/Hardware_system.md#Tiny)")
    if 'Device' in string:
        i+=1
        if i>1:
             i=1
             file.write("<br>")
        file.write("[![1](image/Drive.svg) D&T ](Classification/Hardware_system.md#Tiny)")
    if 'Circuit' in string:
        i+=1
        if i>1:
             i=1
             file.write("<br>")
        file.write("[![1](image/Circuit.svg) Circuit ](Classification/Hardware_system.md#Tiny)")
    
 

def load_metrics(file):

    file.write("## Metrics\n")

    

    path = './res/metrics.json'
    
    with open(path, 'r') as f:
            table = json.load(f)
            file.write("\n")
            file.write("### Metrics overview\n")
            
            file.write("| Metric | Equation | Details | \n")
            file.write(" | :--------| :------ | :------ |\n")

            for metric in table:
                
                    
                    file.write("{}|".format(metric['Description']))
                    file.write(" {}|".format(metric['Equation']))
                    file.write(" {}".format(metric['Details']))
                    
                    file.write("|")
                    file.write("\n")
            file.write("\n")
            file.write("### Metrics application usage\n")
            file.write("|      Metric   | Link | Carbon life cycle stage | Hardware system | Computer system stack | Datacenter stack |  \n")
            file.write("| :--------- | :------| :------ | :------ | :-------- | :-------- | \n")
            for metric in table:
                file.write("|{}".format(metric['Metric']))
                file.write(" |[[Paper]]({})".format(metric['Link']))
                choose(file,metric['Included carbon life cycle stage'])
                choose(file,metric['Hardware system'])
                choose(file,metric['Computer_stack'])
                
                
                choose(file,metric['Datacenter stack'])
                
                
                file.write("|\n")

            
                    
           


    
    



def load_contribute(file):
    with open("./res/contribute.md", 'r') as f:
        for line in f:
            file.write(line)


file = open("./Readme.md", 'w')
file1 = open("./Readme.md", 'w')

load_head(file)

load_legend(file)

load_metrics(file)
load_Link(file)
load_report(file)

#load_lib(file)
load_paper(file)
load_contribute(file)

file.close()


# %%



