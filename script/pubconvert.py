result = []
result.append('<div class="publications"><ol class="bibliography"><li>')
text = open(f"intl-conf.txt").readlines()
for i in range(0, len(text), 3):
    if len(text[i].strip()) == 0: continue
    authors = text[i].strip()
    title = text[i+1].strip()
    text[i+2] = text[i+2].replace(", SCIE", "")
    text[i+2] = text[i+2].replace(", SCI", "")
    venue = text[i+2].strip().split(',')[0] + ' ' + text[i+2].strip().split(',')[-1][-5:-1]
    # print(authors, title, venue)
    result.append(f'<div class="row">\n<div class="col-sm-2 abbr">')
    result.append(f'<abbr class="badge">{venue}</abbr></div>')
    result.append(f'''
      <div id="{venue+title[:5]}" class="col-sm-8">
      
        <div class="title">{title}</div>
        <div class="author">
              {authors}
        </div>
      </div>
    </div>
    ''')
result.append("""
</li></ol>
</div>
""")
result = "\n".join(result)
print(result)