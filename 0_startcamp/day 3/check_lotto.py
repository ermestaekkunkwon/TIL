import lotto_functions
# 혹은 from을 써라 -> result = am_i_lucky(pick_lotto(), get_lotto()) 이렇게만 써도 된다!


result = lotto_functions.am_i_lucky(
    lotto_functions.pick_lotto(),
    lotto_functions.get_lotto(837)
)

print(result)