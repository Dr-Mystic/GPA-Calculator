import streamlit as st

def main():
    st.title('GPA Calculator')

    if 'criteria' not in st.session_state:
        st.session_state.criteria = []
        st.session_state.weights = []
        st.session_state.obtained_marks = []
        st.session_state.total_marks = []

    action = st.selectbox('Select an action', ['Select an action', 'Add Criteria', 'Calculate GPA'])

    if action == 'Add Criteria':
        with st.form('add_criteria_form'):
            criteria_name = st.text_input('Criteria Name')
            weight = st.number_input('Weight (%)', min_value=0.0, max_value=100.0, step=1.0)
            submitted = st.form_submit_button('Add Criteria')

            if submitted:
                if criteria_name and weight:
                    st.session_state.criteria.append(criteria_name)
                    st.session_state.weights.append(weight)
                    st.success(f'Criteria "{criteria_name}" with weight {weight}% added successfully.')
                else:
                    st.error('Please enter valid criteria and weight.')

        st.subheader('Current Criteria')
        for i, (criteria, weight) in enumerate(zip(st.session_state.criteria, st.session_state.weights)):
            with st.expander(f'{criteria} - {weight}%'):
                new_criteria_name = st.text_input(f'Edit Criteria Name {i+1}', value=criteria, key=f'criteria_{i}')
                new_weight = st.number_input(f'Edit Weight {i+1} (%)', value=weight, min_value=0.0, max_value=100.0, step=1.0, key=f'weight_{i}')
                if st.button(f'Delete Criteria {i+1}'):
                    del st.session_state.criteria[i]
                    del st.session_state.weights[i]
                    st.experimental_rerun()
                if new_criteria_name != criteria or new_weight != weight:
                    st.session_state.criteria[i] = new_criteria_name
                    st.session_state.weights[i] = new_weight

    elif action == 'Calculate GPA':
        if sum(st.session_state.weights) != 100:
            st.warning('Total weight of all criteria should be exactly 100%. Please adjust the weights.')
        else:
            st.subheader('Enter Marks for Each Criteria')
            st.session_state.obtained_marks = []
            st.session_state.total_marks = []
            for i in range(len(st.session_state.criteria)):
                criteria = st.session_state.criteria[i]
                obtained_mark = st.number_input(f'Obtained Mark for {criteria}', min_value=0.0, step=1.0, key=f'obtained_mark_{i}')
                total_mark = st.number_input(f'Total Mark for {criteria}', min_value=0.0, step=1.0, key=f'total_mark_{i}')
                st.session_state.obtained_marks.append(obtained_mark)
                st.session_state.total_marks.append(total_mark)

            if st.button('Calculate GPA'):
                weighted_sum = 0
                for obtained_mark, total_mark, weight in zip(st.session_state.obtained_marks, st.session_state.total_marks, st.session_state.weights):
                    if total_mark > 0:
                        percentage = (obtained_mark / total_mark) * 100
                        weighted_sum += (percentage * weight / 100)
                    else:
                        st.error('Total mark must be greater than 0.')
                        return
                
                if weighted_sum >= 86:
                    st.success(f'Your GPA is 4.00 with grade A and {weighted_sum:.2f}%')
                elif weighted_sum >= 82:
                    st.success(f'Your GPA is 3.67 with grade A- and {weighted_sum:.2f}%')
                elif weighted_sum >= 78:
                    st.success(f'Your GPA is 3.33 with grade B+ and {weighted_sum:.2f}%')
                elif weighted_sum >= 74:
                    st.success(f'Your GPA is 3.00 with grade B and {weighted_sum:.2f}%')
                elif weighted_sum >= 70:
                    st.success(f'Your GPA is 2.67 with grade B- and {weighted_sum:.2f}%')
                elif weighted_sum >= 66:
                    st.success(f'Your GPA is 2.33 with grade C+ and {weighted_sum:.2f}%')
                elif weighted_sum >= 62:
                    st.success(f'Your GPA is 2.00 with grade C and {weighted_sum:.2f}%')
                elif weighted_sum >= 58:
                    st.success(f'Your GPA is 1.67 with grade C- and {weighted_sum:.2f}%')
                elif weighted_sum >= 54:
                    st.success(f'Your GPA is 1.33 with grade D+ and {weighted_sum:.2f}%')
                elif weighted_sum >= 50:
                    st.success(f'Your GPA is 1.00 with grade D and {weighted_sum:.2f}%')
                else:
                    st.fail(f'Your GPA is 0.00 with grade F and {weighted_sum:.2f}%')

if __name__ == '__main__':
    main()
