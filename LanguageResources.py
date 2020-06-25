class I18N():
    '''Internationalization'''
    def __init__(self, language):
        if language == 'kr' : self.resourceLanguageKorean()
        elif language == 'en' : self.resourceLanguageEnglish()
        else: raise NotImplementedError('Unsupported Language')

    def resourceLanguageKorean(self):
        self.title = '문장해체분석기'
        self.textEdit = '텍스트 변환'
        self.fileEdit = '파일 변환'
        self.exit = '종료'
        self.exitDescription = '정말로 종료하시겠습니까?'

        self.about = '정보'
        self.aboutTitle =   '  __                    _           _    ' +\
                          '\n (_  o ._ _  ._  |  _  |_)  _   _  |_    ' +\
                          '\n __)  | | | | |_) | (/_ |＼ (/_ (_| |_ >< ' +\
                          '\n             |                  _|       '
        self.aboutDescription = '\n\nDeveloped by kuotient.\nhttps://www.github.com/kuotient'

        self.mngFile = ' 파일 관리 '
        self.settings = ' 설정 '
        self.eliminate = '제거 옵션'
        self.changeable = '변환 옵션'
        self.explain = '※ 특수문자의 경우 변환 이후에 제거가 진행됩니다.'
        self.browse = '찾아보기...'
        self.save = '저장경로 지정 :'
        self.blank = '빈줄'
        self.spChar = '특수문자'
        self.consonants = '모음'
        self.vowels = '자음'
        self.contSpace = '연속적인 공백'
        self.chinese = '한자'
        self.new = '새 프로그램'
        self.settingsMenu = '설정'
        self.file = '파일'
        self.help = '도움말'

    def resourceLanguageEnglish(self):
        self.title = "SimpleRegex"
        self.exit = 'Exit'
        self.textEdit = 'Text Edit'
        self.fileEdit = 'File Edit'
        self.exitDescription = 'Are you sure you want to exit?'

        self.about = 'About'
        self.aboutTitle =   '  __                    _           _    ' +\
                          '\n (_  o ._ _  ._  |  _  |_)  _   _  |_    ' +\
                          '\n __)  | | | | |_) | (/_ |＼ (/_ (_| |_ >< ' +\
                          '\n             |                  _|       '

        self.aboutDescription = '\n\nDeveloped by kuotient.\nhttps://www.github.com/kuotient'

        self.mngFile = ' Mangage Files '
        self.settings = ' Settings '
        self.eliminate = 'Elimination'
        self.changeable = 'Changeables'
        self.explain = 'Changing word is a top priority than any other processes.'
        self.browse = 'Browse to File...'
        self.save = 'Save File to :'
        self.blank = 'Blank'
        self.spChar = 'Special characters'
        self.consonants = 'Consonants'
        self.vowels = 'Vowels'
        self.contSpace = 'Continuous space'
        self.chinese = 'Chinese characters'
        self.new = 'New'
        self.settingsMenu ='Settings'
        self.file = 'File'
        self.help = 'Help'