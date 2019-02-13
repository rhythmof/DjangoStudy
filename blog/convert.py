class year_conv_do:
    regex = r'2[01]\d{2}'

    def to_python(self, value):
        return int(value)
    
    def to_url(self, value):
        return '%04'%value