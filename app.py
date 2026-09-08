query = st.chat_input("Inquire about harmonic intersections, alignments, or node transits...")
 if query:
        st.session_state.messages.append({"role": "user", "content": query})
        with chat_box:
            with st.chat_message("user"):
                st.markdown(query)
            with st.chat_message("assistant"):
                prompt = (
                    f"You are the cartographic and orbital intelligence officer for the Eyerin-Cryoin array, "
                    f"modeled on a 1500s azimuthal equidistant polar disc. "
                    f"Central Hub: Sophia (Node 0). Outer Perimeter: Cryoin Antarctica (Node 12). "
                    f"Currently focused target: [{selected_node['id']}] {selected_node['name']} "
                    f"({selected_node['feature']}) at {selected_node['r']} radius, {selected_node['theta']}° azimuth, "
                    f"vibrating at {selected_node['freq']} Hz. "
                    f"Deliver concise, intriguing, and precise observations."
                )
                try:
                    res = client.models.generate_content(
                        model="gemini-1.5-flash", 
                        contents=[prompt, query]
                    )
                    reply_text = res.text
                except Exception as e:
                    reply_text = f"⚠️ **API Error Details:**\n```\n{e}\n```"
                
                st.markdown(reply_text)
                st.session_state.messages.append({"role": "assistant", "content": reply_text})
