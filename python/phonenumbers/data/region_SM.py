"""Auto-generated file, do not edit by hand. SM metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_SM = PhoneMetadata(id='SM', country_code=378, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[05-7]\\d{7,9}', possible_number_pattern='\\d{6,10}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='0549(?:8[0157-9]|9\\d)\\d{4}', possible_number_pattern='\\d{6,10}', example_number='0549886377'),
    mobile=PhoneNumberDesc(national_number_pattern='6[16]\\d{6}', possible_number_pattern='\\d{8}', example_number='66661212'),
    toll_free=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    premium_rate=PhoneNumberDesc(national_number_pattern='7[178]\\d{6}', possible_number_pattern='\\d{8}', example_number='71123456'),
    shared_cost=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    personal_number=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voip=PhoneNumberDesc(national_number_pattern='5[158]\\d{6}', possible_number_pattern='\\d{8}', example_number='58001110'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    emergency=PhoneNumberDesc(national_number_pattern='11[358]', possible_number_pattern='\\d{3}', example_number='113'),
    voicemail=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    short_code=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    standard_rate=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    national_prefix_for_parsing='(?:0549)?([89]\\d{5})',
    national_prefix_transform_rule='0549\\1',
    number_format=[NumberFormat(pattern='(\\d{2})(\\d{2})(\\d{2})(\\d{2})', format='\\1 \\2 \\3 \\4', leading_digits_pattern=['[5-7]']),
        NumberFormat(pattern='(0549)(\\d{6})', format='\\1 \\2', leading_digits_pattern=['0']),
        NumberFormat(pattern='(\\d{6})', format='0549 \\1', leading_digits_pattern=['[89]'])],
    intl_number_format=[NumberFormat(pattern='(\\d{2})(\\d{2})(\\d{2})(\\d{2})', format='\\1 \\2 \\3 \\4', leading_digits_pattern=['[5-7]']),
        NumberFormat(pattern='(0549)(\\d{6})', format='(\\1) \\2', leading_digits_pattern=['0']),
        NumberFormat(pattern='(\\d{6})', format='(0549) \\1', leading_digits_pattern=['[89]'])],
    leading_zero_possible=True)
